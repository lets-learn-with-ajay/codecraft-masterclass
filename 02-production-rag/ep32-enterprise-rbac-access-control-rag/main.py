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

# Phase 2: Reciprocal Rank Fusion (RRF) & Cross-Encoder Re-Ranking
def reciprocal_rank_fusion(dense_ranks: list[int], sparse_ranks: list[int], k: int = 60) -> list[tuple[int, float]]:
    rrf_scores: dict[int, float] = {}
    for rank, doc_id in enumerate(dense_ranks[:50]):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    for rank, doc_id in enumerate(sparse_ranks[:50]):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    return sorted(rrf_scores.items(), key=lambda item: item[1], reverse=True)

# Phase 3: Groundedness Verification & Citation Guardrail
def verify_citation_grounding(answer_text: str, retrieved_chunks: list[str], min_overlap: float = 0.65) -> dict:
    answer_tokens = set(answer_text.lower().split())
    context_tokens = set(' '.join(retrieved_chunks).lower().split())
    overlap = len(answer_tokens & context_tokens) / max(len(answer_tokens), 1)
    return {
        'grounded': overlap >= min_overlap,
        'attribution_score': round(overlap, 3),
        'chunk_count': len(retrieved_chunks),
    }
