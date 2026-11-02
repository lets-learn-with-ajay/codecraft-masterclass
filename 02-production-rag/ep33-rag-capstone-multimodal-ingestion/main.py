# Phase 2: Late-Interaction MaxSim Token-to-Patch Scoring Engine
def compute_maxsim_score(query_tokens: np.ndarray, page_patches: np.ndarray) -> float:
    sim_matrix = np.matmul(query_tokens, page_patches.T)
    max_per_query_token = np.max(sim_matrix, axis=1)
    return float(np.sum(max_per_query_token))

def rank_visual_pages(query_tokens: np.ndarray, index: dict[str, np.ndarray], top_k: int = 5) -> list[tuple[str, float]]:
    scored = [(pid, compute_maxsim_score(query_tokens, patches)) for pid, patches in index.items()]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:top_k]
