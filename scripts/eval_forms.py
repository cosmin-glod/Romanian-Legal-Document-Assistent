"""Evaluate the form-prefill extractor: natural-language conversation -> fields.

For each gold case we run one extraction pass (temp=0) and compare the
extracted value against the expected value, field by field, with a kind-aware
comparator:
  - structured kinds (cnp, id_series, id_number, date, sex, amount, int, iban)
    and name fields: exact match after diacritic-folding;
  - free-text fields (address, place, description, employer): lenient — all
    significant expected tokens must appear in the extracted value.

Reports field-level accuracy overall / per form / per field-class, plus the
share of cases where every required field is captured in one pass (the rest
fall through to the deterministic manual entry).

Usage:
    uv run python scripts/eval_forms.py
"""

from __future__ import annotations

import json
import sys
import time
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.extractor import extract
from licenta.form_registry import FORMS

GOLD = Path("data/eval/forms_gold.json")
_EXACT_KINDS = {"cnp", "id_series", "id_number", "date", "sex", "amount", "int", "iban"}
_FREE_HINTS = ("address", "place", "description", "employer")


def _fold(s: str) -> str:
    return (
        unicodedata.normalize("NFKD", str(s))
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
        .strip()
    )


def _field_class(form_def, name: str) -> str:
    f = next((x for x in form_def.spec.fields if x.name == name), None)
    if f and f.kind in _EXACT_KINDS:
        return "structured"
    if any(h in name for h in _FREE_HINTS):
        return "freetext"
    return "name"


def _matches(cls: str, expected: str, got) -> bool:
    if got is None:
        return False
    e, g = _fold(expected), _fold(got)
    if cls == "freetext":
        toks = [t for t in e.split() if len(t) > 3]
        return bool(toks) and all(t in g for t in toks)
    return e == g


def main() -> None:
    cases = json.loads(GOLD.read_text())
    rows = []
    for i, c in enumerate(cases, 1):
        fd = FORMS[c["form_id"]]
        res = extract(c["text"], fd)
        per_field = {}
        for name, exp in c["expected"].items():
            cls = _field_class(fd, name)
            got = getattr(res.form, name, None)
            per_field[name] = {
                "cls": cls, "expected": exp, "got": got,
                "ok": _matches(cls, exp, got),
            }
        n_ok = sum(1 for v in per_field.values() if v["ok"])
        n_tot = len(per_field)
        required = {f.name for f in fd.spec.fields if f.required}
        req_ok = all(
            v["ok"] for k, v in per_field.items() if k in required
        )
        rows.append({
            "id": c["id"], "form_id": c["form_id"],
            "fields_ok": n_ok, "fields_total": n_tot,
            "required_complete": req_ok, "per_field": per_field,
        })
        print(f"[{i}/{len(cases)}] {c['id']:16} {n_ok}/{n_tot} fields  "
              f"required_complete={req_ok}", flush=True)

    ts = time.strftime("%Y%m%d_%H%M%S")
    out = Path("data/eval/runs") / f"forms_{ts}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    (out / "report.md").write_text(_report(rows))
    print(f"\nWrote {out}/report.md")


def _pct(n: int, d: int) -> str:
    return f"{100*n/d:.0f}%" if d else "n/a"


def _report(rows) -> str:
    tot_ok = sum(r["fields_ok"] for r in rows)
    tot = sum(r["fields_total"] for r in rows)
    cls_ok: dict[str, int] = {}
    cls_tot: dict[str, int] = {}
    by_form: dict[str, list] = {}
    for r in rows:
        by_form.setdefault(r["form_id"], []).append(r)
        for v in r["per_field"].values():
            cls_tot[v["cls"]] = cls_tot.get(v["cls"], 0) + 1
            cls_ok[v["cls"]] = cls_ok.get(v["cls"], 0) + (1 if v["ok"] else 0)
    req_complete = sum(1 for r in rows if r["required_complete"])

    L = ["# Raport evaluare — pre-completare formulare\n"]
    L.append(f"**Cazuri**: {len(rows)}  ·  **Câmpuri evaluate**: {tot}\n")
    L.append("## Global\n")
    L.append(f"- Acuratețe la nivel de câmp: **{_pct(tot_ok, tot)}** ({tot_ok}/{tot})")
    L.append(f"- Cazuri cu toate câmpurile obligatorii corecte într-o singură rundă: "
             f"**{_pct(req_complete, len(rows))}** ({req_complete}/{len(rows)})\n")
    L.append("## Pe clasă de câmp\n")
    L.append("| Clasă | Corecte / Total | Acuratețe |")
    L.append("|---|---|---|")
    for cls in ("structured", "name", "freetext"):
        if cls in cls_tot:
            L.append(f"| {cls} | {cls_ok[cls]}/{cls_tot[cls]} | "
                     f"{_pct(cls_ok[cls], cls_tot[cls])} |")
    L.append("\n## Pe formular\n")
    L.append("| Formular | Câmpuri corecte | Acuratețe | Req. complet |")
    L.append("|---|---|---|---|")
    for fid, rs in by_form.items():
        ok = sum(r["fields_ok"] for r in rs)
        t = sum(r["fields_total"] for r in rs)
        rc = sum(1 for r in rs if r["required_complete"])
        L.append(f"| {fid} | {ok}/{t} | {_pct(ok, t)} | {rc}/{len(rs)} |")
    # failures
    L.append("\n## Câmpuri ratate\n")
    for r in rows:
        bad = {k: v for k, v in r["per_field"].items() if not v["ok"]}
        if bad:
            L.append(f"\n### {r['id']}")
            for k, v in bad.items():
                L.append(f"- `{k}` ({v['cls']}): aștept `{v['expected']}`, "
                         f"obținut `{v['got']}`")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
