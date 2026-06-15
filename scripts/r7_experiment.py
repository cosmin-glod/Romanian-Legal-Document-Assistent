"""Measure R7 end-to-end: with R7 active in validate(), does the generator's
retry loop recover spurious refusals, while leaving correct refusals untouched?

R7 fires only when a refused answer has a top source similarity >= threshold.
On firing, generate() retries with feedback. We re-run the 21 spurious + 12
control cases (temp=0) and report recoveries vs broken controls.

Usage:
    uv run python scripts/r7_experiment.py <baseline_run_dir>
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.generator import generate
from licenta.retriever import Retriever

GOLD = Path("data/eval/gold_set.json")


def main() -> None:
    baseline_dir = Path(sys.argv[1])
    results = json.loads((baseline_dir / "results.json").read_text())
    gold = {c["id"]: c for c in json.loads(GOLD.read_text())}

    spurious = [r["case_id"] for r in results if r["is_refusal"] and not r["should_refuse"]]
    control = [r["case_id"] for r in results if r["should_refuse"]]
    base_refused = {r["case_id"]: r["is_refusal"] for r in results}
    target = spurious + control

    retriever = Retriever()
    rows = []
    for i, cid in enumerate(target, 1):
        case = gold[cid]
        hits = retriever.query(case["question"], k=4)
        a = generate(case["question"], hits, temperature=0.0)  # R7 active in validate
        r7 = any(v.rule_id == "R7_OVERREFUSAL" for v in a.violations)
        rows.append(
            {
                "id": cid,
                "subset": "control" if case.get("should_refuse") else "spurious",
                "base_refused": base_refused[cid],
                "r7_fired_final": r7,
                "final_refused": a.schema.is_refusal,
                "attempts": a.attempts,
            }
        )
        print(
            f"[{i}/{len(target)}] {cid} ({rows[-1]['subset']}): "
            f"base_refuse={base_refused[cid]} -> final_refuse={a.schema.is_refusal} "
            f"(attempts={a.attempts})",
            flush=True,
        )

    out = baseline_dir.parent / f"r7_experiment_{time.strftime('%Y%m%d_%H%M%S')}.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))

    spur = [r for r in rows if r["subset"] == "spurious"]
    ctrl = [r for r in rows if r["subset"] == "control"]
    recovered = sum(1 for r in spur if not r["final_refused"])
    ctrl_kept = sum(1 for r in ctrl if r["base_refused"] and r["final_refused"])
    ctrl_base = sum(1 for r in ctrl if r["base_refused"])
    print("\n==== RESULT (R7 + retry) ====")
    print(f"spurious recovered: {recovered}/{len(spur)}")
    print(f"control correct refusals kept: {ctrl_kept}/{ctrl_base}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
