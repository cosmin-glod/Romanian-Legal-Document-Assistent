"""Run the evaluation harness over the gold set.

Usage:
    uv run python scripts/eval.py                  # full run, default model
    uv run python scripts/eval.py --limit 3        # smoke test, first 3 cases
    uv run python scripts/eval.py -m qwen2.5:7b-instruct-q4_K_M
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.evaluate import run
from licenta.generator import DEFAULT_MODEL


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--gold",
        default="data/eval/gold_set.json",
        help="path to gold-set JSON",
    )
    p.add_argument(
        "--out",
        default=None,
        help="output directory (default: data/eval/runs/<timestamp>_<model>)",
    )
    p.add_argument("-k", type=int, default=4, help="number of chunks to retrieve")
    p.add_argument("-m", "--model", default=DEFAULT_MODEL)
    p.add_argument(
        "--limit", type=int, default=None, help="evaluate only the first N cases"
    )
    p.add_argument(
        "--temp",
        type=float,
        default=0.2,
        help="generation temperature (0 = deterministic, reproducible)",
    )
    p.add_argument(
        "--fewshot",
        action="store_true",
        help="prepend few-shot exemplars to the generation prompt",
    )
    args = p.parse_args()

    logging.basicConfig(level=logging.WARNING, format="%(message)s")

    if args.out is None:
        ts = time.strftime("%Y%m%d_%H%M%S")
        model_slug = args.model.replace(":", "_").replace("/", "_")
        out = Path("data/eval/runs") / f"{ts}_{model_slug}"
    else:
        out = Path(args.out)

    md_path = run(
        gold_set_path=Path(args.gold),
        output_dir=out,
        model=args.model,
        k=args.k,
        limit=args.limit,
        temperature=args.temp,
        few_shot=args.fewshot,
    )
    print(f"\nDone. Open the report: {md_path}")


if __name__ == "__main__":
    main()
