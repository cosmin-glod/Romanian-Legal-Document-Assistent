"""D2 experiment: does a refusal-calibrated system prompt recover spurious
refusals without breaking correct (out-of-domain) refusals?

Targeted, deterministic (temp=0). Runs only the cases that matter:
  - spurious refusals on the baseline run (should_refuse=False but the model
    refused) — we want these to flip to a grounded answer;
  - control cases (should_refuse=True) — these MUST stay refused.

For each case we generate twice: baseline SYSTEM_PROMPT vs REFINED prompt,
and report refusal accuracy on each subset.

Usage:
    uv run python scripts/refusal_experiment.py <baseline_run_dir>
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.generator import SYSTEM_PROMPT_TEMPLATE, generate
from licenta.form_registry import form_catalog_for_prompt
from licenta.retriever import Retriever

GOLD = Path("data/eval/gold_set.json")

# The baseline rule 4 (over-refuses) vs a calibrated version that tells the
# model to answer whenever the sources contain the information, even partially,
# and to refuse only when the topic is entirely absent.
_BASELINE_RULE4 = (
    '4. Dacă SURSELE nu conțin răspunsul, setează is_refusal=true și răspunde: '
    '"Nu am suficiente informații în sursele disponibile pentru a răspunde."'
)
_REFINED_RULE4 = (
    '4. Înainte de a refuza, recitește SURSELE. Dacă ele conțin informația '
    'cerută — chiar și parțial sau formulată diferit — TREBUIE să răspunzi pe '
    'baza lor și să citezi sursa; NU refuza. Setează is_refusal=true DOAR dacă '
    'subiectul întrebării lipsește complet din SURSE. În caz de dubiu, când '
    'există cel puțin o sursă relevantă, răspunde în loc să refuzi. Mesajul de '
    'refuz, când se aplică: "Nu am suficiente informații în sursele disponibile '
    'pentru a răspunde."'
)


def _build_prompt(refined: bool) -> str:
    template = SYSTEM_PROMPT_TEMPLATE
    if refined:
        assert _BASELINE_RULE4 in template, "baseline rule 4 text drifted"
        template = template.replace(_BASELINE_RULE4, _REFINED_RULE4)
    return template.format(forms_catalog=form_catalog_for_prompt())


def main() -> None:
    baseline_dir = Path(sys.argv[1])
    results = json.loads((baseline_dir / "results.json").read_text())
    gold = {c["id"]: c for c in json.loads(GOLD.read_text())}

    spurious = [
        r["case_id"]
        for r in results
        if r["is_refusal"] and not r["should_refuse"]
    ]
    control = [r["case_id"] for r in results if r["should_refuse"]]
    target_ids = spurious + control
    print(f"spurious={len(spurious)}  control={len(control)}")

    # baseline is_refusal is already known from the stored run; only the
    # refined prompt needs fresh generation.
    base_refused = {r["case_id"]: r["is_refusal"] for r in results}

    retriever = Retriever()
    refined_prompt = _build_prompt(refined=True)

    rows = []
    for i, cid in enumerate(target_ids, 1):
        case = gold[cid]
        hits = retriever.query(case["question"], k=4)
        a_ref = generate(
            case["question"], hits, temperature=0.0, system_prompt=refined_prompt
        )
        should = case.get("should_refuse", False)
        rows.append(
            {
                "id": cid,
                "subset": "control" if should else "spurious",
                "should_refuse": should,
                "base_refused": base_refused[cid],
                "refined_refused": a_ref.schema.is_refusal,
                "refined_answer": a_ref.text[:160],
            }
        )
        print(
            f"[{i}/{len(target_ids)}] {cid} ({rows[-1]['subset']}): "
            f"base_refuse={base_refused[cid]} -> "
            f"refined_refuse={a_ref.schema.is_refusal}",
            flush=True,
        )

    out = baseline_dir.parent / f"refusal_experiment_{time.strftime('%Y%m%d_%H%M%S')}.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))

    spur = [r for r in rows if r["subset"] == "spurious"]
    ctrl = [r for r in rows if r["subset"] == "control"]
    recovered = sum(1 for r in spur if not r["refined_refused"])
    ctrl_kept = sum(1 for r in ctrl if r["refined_refused"])
    print("\n==== RESULT ====")
    print(
        f"spurious recovered (refuse->answer): {recovered}/{len(spur)} "
        f"({100*recovered/max(len(spur),1):.0f}%)"
    )
    print(
        f"control still refused (kept correct): {ctrl_kept}/{len(ctrl)} "
        f"({100*ctrl_kept/max(len(ctrl),1):.0f}%)"
    )
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
