# Phase 1: Dual-Index Hybrid Retrieval (Dense HNSW + Sparse BM25)
from rank_bm25 import BM25Okapi
import numpy as np

class HybridVectorIndex:
    def __init__(self, corpus_docs: list[str], dense_vectors: np.ndarray):
        self.corpus_docs = corpus_docs
        self.dense_vectors = dense_vectors
        self.bm25 = BM25Okapi([doc.lower().split() for doc in corpus_docs])

    def score_candidates(self, query_text: str, query_vec: np.ndarray) -> tuple[list[int], list[int]]:
        bm25_scores = self.bm25.get_scores(query_text.lower().split())
        dense_scores = np.dot(self.dense_vectors, query_vec)
        return list(np.argsort(dense_scores)[::-1]), list(np.argsort(bm25_scores)[::-1])
