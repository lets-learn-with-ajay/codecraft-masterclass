# Phase 2: Reciprocal Rank Fusion (RRF) Scoring
def reciprocal_rank_fusion(dense_ranks, bm25_ranks, k: int = 60) -> list:
    '''Fuses multiple ranked lists without requiring score normalization.'''
    rrf_scores = {}
    for rank, doc_id in enumerate(dense_ranks):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + (1.0 / (k + rank + 1))
    for rank, doc_id in enumerate(bm25_ranks):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + (1.0 / (k + rank + 1))
    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
