"""Section → chunk conversion for RAG indexing.

One chunk per section is the default; oversized sections are split greedily at
sentence boundaries with a hard MAX_CHARS cap. Every chunk carries the
breadcrumb as a prefix so the embedding picks up structural context and so
retrieved snippets stay self-locating when shown to the user.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

# ~750 tokens for Romanian text. Comfortable for bge-m3 (max 8192) while
# small enough that retrieval stays precise.
MAX_CHARS = 3000


@dataclass
class Chunk:
    chunk_id: str
    slug: str
    title: str
    url: str
    breadcrumb: list[str]
    heading: str
    text: str


def _breadcrumb_prefix(breadcrumb: list[str]) -> str:
    return "[" + " > ".join(breadcrumb) + "]"


def _section_body(section_text: str, bullets: list[str]) -> str:
    parts: list[str] = []
    if section_text:
        parts.append(section_text)
    if bullets:
        parts.append("\n".join(f"- {b}" for b in bullets))
    return "\n\n".join(parts).strip()


_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def _split_to_fit(text: str, max_chars: int) -> list[str]:
    """Greedy sentence-boundary split. If a single sentence exceeds max_chars
    (rare), it goes through as one piece — better an oversized chunk than mid-
    sentence truncation."""
    if len(text) <= max_chars:
        return [text]
    pieces: list[str] = []
    current = ""
    for sentence in _SENT_SPLIT.split(text):
        candidate = f"{current} {sentence}".strip() if current else sentence
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                pieces.append(current)
            current = sentence
    if current:
        pieces.append(current)
    return pieces


def chunk_section(
    *, slug: str, title: str, url: str, section_idx: int, section: dict
) -> list[Chunk]:
    breadcrumb = section["breadcrumb"]
    heading = section["heading"]
    prefix = _breadcrumb_prefix(breadcrumb)

    body = _section_body(section["text"], section["bullets"])
    if not body:
        return []

    # Reserve space for the prefix in every piece.
    budget = MAX_CHARS - len(prefix) - 16  # 16 ≈ "\n (parte i/n)\n"
    pieces = _split_to_fit(body, budget)

    chunks: list[Chunk] = []
    for i, piece in enumerate(pieces):
        part_suffix = f" (parte {i + 1}/{len(pieces)})" if len(pieces) > 1 else ""
        chunk_id = f"{slug}:{section_idx}" + (f":{i}" if len(pieces) > 1 else "")
        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                slug=slug,
                title=title,
                url=url,
                breadcrumb=breadcrumb,
                heading=heading,
                text=f"{prefix}{part_suffix}\n{piece}",
            )
        )
    return chunks


def chunk_dump(dump_path: Path) -> list[Chunk]:
    docs = json.loads(dump_path.read_text())
    out: list[Chunk] = []
    for doc in docs:
        for idx, section in enumerate(doc["sections"]):
            out.extend(
                chunk_section(
                    slug=doc["slug"],
                    title=doc["title"],
                    url=doc["url"],
                    section_idx=idx,
                    section=section,
                )
            )
    return out


if __name__ == "__main__":
    import sys

    chunks = chunk_dump(Path("data/cezicelegea_dump.json"))
    print(f"Total chunks: {len(chunks)}")
    by_slug: dict[str, int] = {}
    for c in chunks:
        by_slug[c.slug] = by_slug.get(c.slug, 0) + 1
    for slug, n in by_slug.items():
        print(f"  {slug}: {n} chunks")
    sizes = sorted(len(c.text) for c in chunks)
    print(
        f"Chunk size chars: min={sizes[0]}  median={sizes[len(sizes)//2]}  "
        f"max={sizes[-1]}  avg={sum(sizes)//len(sizes)}"
    )
    if "--sample" in sys.argv:
        print("\n--- sample chunk (middle) ---")
        print(chunks[len(chunks) // 2].text[:800])
