"""Regenerate data/eval/retrieval_scores.json (feeds fig_score_dist, fig_r7_sweep
and the R7 threshold calibration).

For every gold case it records the top-1 retrieval similarity together with the
refusal labels, so the R7 score distribution can be rebuilt for the current
corpus and gold set. Retrieval-only (no LLM): the `is_refusal` decision is taken
from a baseline run's results.json, joined by case id.

Usage:
    PYTHONPATH=src python scripts/retrieval_scores.py <baseline_run_dir>
        e.g. scripts/retrieval_scores.py data/results/3b_q4
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.retriever import Retriever

GOLD = Path("data/eval/gold_set.json")
OUT = Path("data/eval/retrieval_scores.json")


def main() -> None:
    baseline_dir = Path(sys.argv[1])
    results = json.loads((baseline_dir / "results.json").read_text())
    refused = {r["case_id"]: bool(r["is_refusal"]) for r in results}
    gold = json.loads(GOLD.read_text())

    retriever = Retriever()
    rows = []
    for c in gold:
        cid = c["id"]
        if cid not in refused:
            continue  # case not present in the baseline run
        hits = retriever.query(c["question"], k=1)
        top1 = hits[0].score if hits else 0.0
        rows.append(
            {
                "id": cid,
                "top1": top1,
                "is_refusal": refused[cid],
                "should_refuse": bool(c.get("should_refuse", False)),
            }
        )

    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    spur = sum(1 for r in rows if r["is_refusal"] and not r["should_refuse"])
    corr = sum(1 for r in rows if r["is_refusal"] and r["should_refuse"])
    print(f"Wrote {OUT}  (n={len(rows)}; spurious_refuz={spur}, refuz_corect={corr})")


if __name__ == "__main__":
    main()
