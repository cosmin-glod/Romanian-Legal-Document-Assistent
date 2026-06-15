"""A5: true contracts-OFF vs contracts-ON ablation.

For each gold case we generate once with retry enabled (temp=0) and record:
  - first_attempt_violations  -> what "contracts OFF" would have served as-is;
  - final violations          -> after the retry the contract layer triggers.

Contracts OFF  = serve the first model answer regardless.
Contracts ON   = retry on violation; if still invalid, WITHHOLD (controlled refusal).

We report how many wrong answers reach the citizen in each regime.

Usage:
    uv run python scripts/ablation_contracts.py
"""

from __future__ import annotations

import json
import time
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.generator import generate
from licenta.retriever import Retriever

GOLD = Path("data/eval/gold_set.json")
OUT = Path("data/eval/ablation_contracts.json")


def main() -> None:
    cases = json.loads(GOLD.read_text())
    retriever = Retriever()

    rows = []
    for i, c in enumerate(cases, 1):
        hits = retriever.query(c["question"], k=4)
        a = generate(c["question"], hits, temperature=0.0, max_retries=1)
        off_v = [v.rule_id for v in a.first_attempt_violations]
        on_v = [v.rule_id for v in a.violations]
        rows.append(
            {
                "id": c["id"],
                "off_violations": off_v,   # served if layer OFF
                "on_violations": on_v,     # remaining after retry (would be withheld)
                "attempts": a.attempts,
            }
        )
        print(
            f"[{i}/{len(cases)}] {c['id']}: off={len(off_v)} on={len(on_v)} "
            f"attempts={a.attempts}",
            flush=True,
        )

    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2))

    n = len(rows)
    off_bad = sum(1 for r in rows if r["off_violations"])
    fixed = sum(1 for r in rows if r["off_violations"] and not r["on_violations"])
    withheld = sum(1 for r in rows if r["on_violations"])
    print("\n==== ABLATION RESULT ====")
    print(f"n = {n}")
    print(f"OFF: wrong answers served to citizen: {off_bad}/{n} ({100*off_bad/n:.0f}%)")
    print(f"ON : auto-corrected by retry: {fixed}")
    print(f"ON : withheld (controlled refusal): {withheld}")
    print(f"ON : wrong answers served to citizen: 0 (all withheld or fixed)")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
