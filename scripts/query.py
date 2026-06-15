"""Quick CLI to sanity-check retrieval.

Usage:
    uv run python scripts/query.py "ce documente imi trebuie pentru certificatul de nastere?"
    uv run python scripts/query.py -k 3 -s casatorie "varsta minima"
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from licenta.retriever import Retriever


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("query", help="natural-language question (Romanian)")
    p.add_argument("-k", type=int, default=5, help="number of hits")
    p.add_argument("-s", "--slug", choices=["nastere", "casatorie", "locuire"], default=None)
    p.add_argument("--full", action="store_true", help="print full chunk text instead of preview")
    args = p.parse_args()

    logging.basicConfig(level=logging.WARNING, format="%(message)s")
    r = Retriever()
    hits = r.query(args.query, k=args.k, slug=args.slug)

    print(f"\nQuery: {args.query}")
    if args.slug:
        print(f"Filtered to slug: {args.slug}")
    print("-" * 80)
    for i, h in enumerate(hits, 1):
        m = h.metadata
        print(f"\n[{i}] score={h.score:.3f}  id={h.chunk_id}")
        print(f"    breadcrumb: {m['breadcrumb']}")
        if args.full:
            print(h.text)
        else:
            preview = h.text.replace("\n", " ")[:240]
            print(f"    {preview}...")


if __name__ == "__main__":
    main()

