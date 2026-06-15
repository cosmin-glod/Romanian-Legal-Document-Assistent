"""R4 hardening ablation: re-score a stored eval run under the hardened R4 rule.

The hardened R4 (contracts._rule_documents_grounded) normalizes diacritics and
tolerates Romanian inflection via prefix-token matching, instead of the old
plain case-insensitive substring test. Because the instrumented eval persists
`documents_mentioned` + `cited_sources_text`, we can re-score R4 offline — no
model re-run needed — and compare before (stored `violations`) vs after.

Usage:
    uv run python scripts/r4_ablation.py data/eval/runs/<run_dir>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.contracts import _document_is_grounded, _significant_tokens


def hardened_r4_count(case: dict) -> int:
    if not case["documents_mentioned"] or not case["cited_source_indices"]:
        return 0
    src_tokens = set(_significant_tokens(" ".join(case["cited_sources_text"])))
    return sum(
        1
        for doc in case["documents_mentioned"]
        if len(doc.strip()) >= 6 and not _document_is_grounded(doc, src_tokens)
    )


def main() -> None:
    run_dir = Path(sys.argv[1])
    data = json.loads((run_dir / "results.json").read_text())

    old_cases, new_cases = set(), set()
    old_occ = new_occ = 0
    for r in data:
        o = r["violations"].count("R4_FABRICATED_DOC")
        n = hardened_r4_count(r)
        if o:
            old_cases.add(r["case_id"])
            old_occ += o
        if n:
            new_cases.add(r["case_id"])
            new_occ += n

    n = len(data)
    old_pass = sum(1 for r in data if r["contract_valid"])
    new_pass = sum(
        1
        for r in data
        if not [v for v in r["violations"] if v != "R4_FABRICATED_DOC"]
        and hardened_r4_count(r) == 0
    )

    print(f"Run: {run_dir.name}  (n={n})")
    print(f"R4 occurrences: {old_occ} -> {new_occ}")
    print(f"R4 cases:       {len(old_cases)} -> {len(new_cases)}")
    print(f"  cleared:      {sorted(old_cases - new_cases)}")
    print(f"  newly flagged:{sorted(new_cases - old_cases)}")
    print(
        f"Contract pass:  {old_pass}/{n} ({100*old_pass/n:.0f}%) -> "
        f"{new_pass}/{n} ({100*new_pass/n:.0f}%)"
    )


if __name__ == "__main__":
    main()
