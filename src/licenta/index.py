"""Build the Chroma index from the cezicelegea dump.

Uses BAAI/bge-m3 — multilingual embedding model with strong Romanian
performance and no required query/passage prefix. Embeddings are L2-normalized
so cosine ≡ dot product in Chroma.

First run downloads ~2.3GB (model weights, cached under ~/.cache/huggingface).
Subsequent runs are local. The whole index for ~150 chunks builds in under a
minute on M1 CPU.
"""

from __future__ import annotations

import logging
import os
import shutil
from dataclasses import asdict
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from licenta.chunker import Chunk, chunk_dump

# Override via env (e.g. LICENTA_CHROMA_DIR=/tmp/chroma on Kaggle, where ChromaDB 1.5
# Rust cannot write under /kaggle/working -> "attempt to write a readonly database").
CHROMA_DIR = Path(os.environ.get("LICENTA_CHROMA_DIR", "data/chroma_db"))
COLLECTION = "cezicelegea"
EMBED_MODEL = "BAAI/bge-m3"

log = logging.getLogger(__name__)


def _metadata_for(chunk: Chunk) -> dict:
    # Chroma metadata values must be primitives — flatten the breadcrumb.
    return {
        "chunk_id": chunk.chunk_id,
        "slug": chunk.slug,
        "title": chunk.title,
        "url": chunk.url,
        "heading": chunk.heading,
        "breadcrumb": " > ".join(chunk.breadcrumb),
    }


def build_index(
    dump_path: Path = Path("data/cezicelegea_dump.json"),
    chroma_dir: Path = CHROMA_DIR,
    model_name: str = EMBED_MODEL,
    reset: bool = True,
) -> None:
    chunks = chunk_dump(dump_path)
    log.info("chunks: %d", len(chunks))

    if reset and chroma_dir.exists():
        log.info("removing existing index at %s", chroma_dir)
        shutil.rmtree(chroma_dir)

    log.info("loading embedding model: %s", model_name)
    model = SentenceTransformer(model_name)
    log.info("embedding dim: %d", model.get_sentence_embedding_dimension())

    log.info("encoding %d chunks...", len(chunks))
    embeddings = model.encode(
        [c.text for c in chunks],
        normalize_embeddings=True,
        show_progress_bar=True,
        batch_size=8,
    )

    chroma_dir.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(chroma_dir))
    collection = client.get_or_create_collection(
        COLLECTION, metadata={"hnsw:space": "cosine"}
    )
    collection.add(
        ids=[c.chunk_id for c in chunks],
        embeddings=embeddings.tolist(),
        documents=[c.text for c in chunks],
        metadatas=[_metadata_for(c) for c in chunks],
    )
    log.info("wrote %d vectors to %s", len(chunks), chroma_dir)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    build_index()
