"""Retrieve top-k chunks from the Chroma index for a query.

Reusable from a CLI, a notebook, or later the chat endpoint.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from licenta.index import CHROMA_DIR, COLLECTION, EMBED_MODEL

log = logging.getLogger(__name__)


@dataclass
class Hit:
    chunk_id: str
    score: float  # cosine similarity in [-1, 1]; higher = more relevant
    text: str
    metadata: dict


class Retriever:
    def __init__(
        self,
        chroma_dir: Path = CHROMA_DIR,
        model_name: str = EMBED_MODEL,
        collection_name: str = COLLECTION,
    ) -> None:
        log.info("loading embedding model: %s", model_name)
        self.model = SentenceTransformer(model_name)
        self.client = chromadb.PersistentClient(path=str(chroma_dir))
        self.collection = self.client.get_collection(collection_name)

    def query(self, text: str, k: int = 5, slug: str | None = None) -> list[Hit]:
        embedding = self.model.encode(text, normalize_embeddings=True).tolist()
        where = {"slug": slug} if slug else None
        res = self.collection.query(
            query_embeddings=[embedding], n_results=k, where=where
        )
        hits: list[Hit] = []
        for i, doc in enumerate(res["documents"][0]):
            distance = res["distances"][0][i]  # cosine distance = 1 - similarity
            hits.append(
                Hit(
                    chunk_id=res["ids"][0][i],
                    score=1.0 - distance,
                    text=doc,
                    metadata=res["metadatas"][0][i],
                )
            )
        return hits
