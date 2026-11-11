# Phase 1: ColPali Vision-Language Patch Grid Embedding Normalization
import numpy as np

class ColPaliPageIndex:
    def __init__(self, embed_dim: int = 128):
        self.embed_dim = embed_dim
        self.page_patches: dict[str, np.ndarray] = {}

    def index_page(self, page_id: str, raw_patches: np.ndarray) -> None:
        norms = np.linalg.norm(raw_patches, axis=1, keepdims=True) + 1e-8
        self.page_patches[page_id] = (raw_patches / norms).astype(np.float32)

# Phase 2: Late-Interaction MaxSim Token-to-Patch Scoring Engine
def compute_maxsim_score(query_tokens: np.ndarray, page_patches: np.ndarray) -> float:
    sim_matrix = np.matmul(query_tokens, page_patches.T)
    max_per_query_token = np.max(sim_matrix, axis=1)
    return float(np.sum(max_per_query_token))

def rank_visual_pages(query_tokens: np.ndarray, index: dict[str, np.ndarray], top_k: int = 5) -> list[tuple[str, float]]:
    scored = [(pid, compute_maxsim_score(query_tokens, patches)) for pid, patches in index.items()]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:top_k]

# Phase 3: 1-Bit Binary Quantization for 32x Patch Memory Compression
def quantize_patches_binary(float_patches: np.ndarray) -> np.ndarray:
    binary_bits = (float_patches > 0.0).astype(np.uint8)
    return np.packbits(binary_bits, axis=-1)
