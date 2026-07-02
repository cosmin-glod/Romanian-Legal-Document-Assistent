"""Smoke-test the form engine: validate + render every form in the catalog
from synthetic data. No LLM involved — exercises schema, validator, renderer.

Usage:
    uv run python scripts/form.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.form_registry import FORMS

OUT_DIR = Path("data/forms")

_SAMPLE = {
    "text": "Ion Popescu",
    "textarea": "Apartament 2 camere, etaj 3",
    "cnp": "1900101123456",
    "id_series": "RT",
    "id_number": "123456",
    "date": "25.05.2026",
    "sex": "M",
    "iban": "RO49AAAA1B31007593840000",
    "amount": "1500",
    "int": "10",
}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ok = 0
    for form_id, defn in FORMS.items():
        values = {f.name: _SAMPLE.get(f.kind, "Exemplu") for f in defn.spec.fields}
        form = defn.schema(**values)
        errors = defn.validate_fn(form)
        if errors:
            print(f"[FAIL] {form_id}: validation errors: {errors}")
            continue
        out = OUT_DIR / f"sample_{form_id}.pdf"
        defn.render_fn(form, out)
        print(f"[ OK ] {form_id:30} -> {out}  ({out.stat().st_size} bytes)")
        ok += 1
    print(f"\n{ok}/{len(FORMS)} forms rendered.")


if __name__ == "__main__":
    main()
