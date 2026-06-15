"""Tier-1 #2: does few-shot prompting reduce spurious refusal?

Targeted, deterministic (temp=0), fair (baseline + few-shot generated fresh per
case, identical retrieval). Mirrors the D2 refusal-calibration experiment so the
two interventions are directly comparable.

Target set: the spurious refusals on a prior run (should_refuse=False but
refused) + the controls (should_refuse=True). We want few-shot to flip spurious
refusals to answers while keeping correct refusals.

Usage:
    uv run python scripts/fewshot_experiment.py <baseline_run_dir>
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.generator import FEW_SHOT, generate
from licenta.retriever import Retriever

GOLD = Path("data/eval/gold_set.json")


def main() -> None:
    baseline_dir = Path(sys.argv[1])
    prior = json.loads((baseline_dir / "results.json").read_text())
    gold = {c["id"]: c for c in json.loads(GOLD.read_text())}

    spurious = [r["case_id"] for r in prior if r["is_refusal"] and not r["should_refuse"]]
    control = [r["case_id"] for r in prior if r["should_refuse"]]
    target = spurious + control
    print(f"spurious={len(spurious)}  control={len(control)}")

    retriever = Retriever()
    rows = []
    for i, cid in enumerate(target, 1):
        case = gold[cid]
        hits = retriever.query(case["question"], k=4)
        base = generate(case["question"], hits, temperature=0.0)
        fs = generate(case["question"], hits, temperature=0.0, history=FEW_SHOT)
        rows.append({
            "id": cid,
            "subset": "control" if case.get("should_refuse") else "spurious",
            "base_refused": base.schema.is_refusal,
            "fewshot_refused": fs.schema.is_refusal,
            "fewshot_answer": fs.text[:140],
        })
        print(f"[{i}/{len(target)}] {cid} ({rows[-1]['subset']}): "
              f"base={base.schema.is_refusal} -> fewshot={fs.schema.is_refusal}",
              flush=True)

    out = baseline_dir.parent / f"fewshot_experiment_{time.strftime('%Y%m%d_%H%M%S')}.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))

    spur = [r for r in rows if r["subset"] == "spurious"]
    ctrl = [r for r in rows if r["subset"] == "control"]
    # recovered: was refused at baseline (this fresh run), now answers
    base_ref_spur = [r for r in spur if r["base_refused"]]
    recovered = sum(1 for r in base_ref_spur if not r["fewshot_refused"])
    base_ref_ctrl = [r for r in ctrl if r["base_refused"]]
    ctrl_kept = sum(1 for r in base_ref_ctrl if r["fewshot_refused"])
    print("\n==== RESULT (few-shot) ====")
    print(f"spurious refused at baseline: {len(base_ref_spur)}/{len(spur)}")
    print(f"  recovered by few-shot (refuse->answer): {recovered}/{len(base_ref_spur)}")
    print(f"control correct refusals kept: {ctrl_kept}/{len(base_ref_ctrl)}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
