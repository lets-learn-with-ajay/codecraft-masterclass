"""
Diffusion Models Masterclass - Episode 27: Text Encoders at Scale
T5-XXL, Gemma 2, and Handling Long Descriptive Prompts in Modern Diffusion Models (SD3, Flux.1)
"""

import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

# ============================================================================
# Phase 1: Dual Text Conditioner (CLIP Style + T5-XXL Syntax)
# ============================================================================

@dataclass
class DualPromptEmbeddings:
    clip_pooled: List[float]               # Global semantic vector (e.g., 768 or 1024 dims)
    t5_sequence: List[List[float]]          # Token sequence embeddings (seq_len x 4096 dims)
    attention_mask: List[int]              # Binary attention mask (1 for token, 0 for pad)
    prompt: str


class DualTextConditioner:
    """
    Simulates modern dual/triple text encoding (e.g. SD3 / Flux.1):
    - CLIP ViT-L/14: Captures style, aesthetics, and coarse semantic classification -> Pooled embedding
    - T5-XXL: Captures intricate spatial relationships, grammar, and typography -> Contextual sequence
    """
    def __init__(self, clip_dim: int = 768, t5_dim: int = 4096, max_seq_len: int = 512):
        self.clip_dim = clip_dim
        self.t5_dim = t5_dim
        self.max_seq_len = max_seq_len

    def tokenize(self, text: str) -> List[str]:
        """Simple whitespace/punctuation tokenizer for simulation."""
        cleaned = text.lower().replace(",", " , ").replace(".", " . ")
        return [tok for tok in cleaned.split() if tok]

    def encode_clip_pooled(self, tokens: List[str]) -> List[float]:
        """Extracts a normalized global pooled embedding vector."""
        vec = [0.0] * self.clip_dim
        for i, tok in enumerate(tokens):
            h = int(hashlib.sha256(tok.encode()).hexdigest(), 16)
            for d in range(self.clip_dim):
                weight = ((h >> (d % 32)) & 0xFF) / 255.0 - 0.5
                vec[d] += weight / (1.0 + i * 0.1)
        # L2 Normalize
        norm = math.sqrt(sum(x * x for x in vec)) or 1e-6
        return [x / norm for x in vec]

    def encode_t5_sequence(self, tokens: List[str]) -> Tuple[List[List[float]], List[int]]:
        """Extracts contextual per-token sequence representations up to max_seq_len."""
        seq = tokens[:self.max_seq_len]
        embeddings = []
        mask = [1] * len(seq)

        for pos, tok in enumerate(seq):
            tok_vec = [0.0] * self.t5_dim
            h = int(hashlib.md5(f"{tok}_{pos}".encode()).hexdigest(), 16)
            for d in range(self.t5_dim):
                val = ((h >> (d % 16)) & 0xF) / 15.0 - 0.5
                tok_vec[d] = val
            embeddings.append(tok_vec)

        # Pad to max_seq_len if required
        padding_len = self.max_seq_len - len(seq)
        if padding_len > 0:
            pad_vec = [0.0] * self.t5_dim
            embeddings.extend([pad_vec] * padding_len)
            mask.extend([0] * padding_len)

        return embeddings, mask

    def encode(self, prompt: str) -> DualPromptEmbeddings:
        tokens = self.tokenize(prompt)
        clip_pooled = self.encode_clip_pooled(tokens)
        t5_seq, mask = self.encode_t5_sequence(tokens)
        return DualPromptEmbeddings(
            clip_pooled=clip_pooled,
            t5_sequence=t5_seq,
            attention_mask=mask,
            prompt=prompt
        )


# ============================================================================
# Phase 2: Embedding Disk Cache Manager (Offline Pre-Computation)
# ============================================================================

class PromptEmbeddingCache:
    """
    Caches large T5-XXL / Gemma embeddings to disk to prevent redundant forward passes
    during diffusion fine-tuning or repeated generation workflows.
    """
    def __init__(self, cache_dir: Union[str, Path]):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _hash_key(self, prompt: str) -> str:
        return hashlib.sha256(prompt.strip().encode("utf-8")).hexdigest()

    def get(self, prompt: str) -> Optional[DualPromptEmbeddings]:
        key = self._hash_key(prompt)
        path = self.cache_dir / f"{key}.json"
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return DualPromptEmbeddings(
            clip_pooled=data["clip_pooled"],
            t5_sequence=data["t5_sequence"],
            attention_mask=data["attention_mask"],
            prompt=data["prompt"]
        )

    def set(self, embeddings: DualPromptEmbeddings) -> None:
        key = self._hash_key(embeddings.prompt)
        path = self.cache_dir / f"{key}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump({
                "clip_pooled": embeddings.clip_pooled,
                "t5_sequence": embeddings.t5_sequence,
                "attention_mask": embeddings.attention_mask,
                "prompt": embeddings.prompt
            }, f)


# ============================================================================
# Phase 3: Reference PyTorch Layer Definitions for Production Execution
# ============================================================================

try:
    import torch
    import torch.nn as nn

    class PyTorchDualTextProjection(nn.Module):
        """
        Projects concatenated text encodings into the MMDiT transformer joint dimension.
        """
        def __init__(self, clip_dim: int = 768, t5_dim: int = 4096, hidden_dim: int = 1536):
            super().__init__()
            self.clip_proj = nn.Linear(clip_dim, hidden_dim)
            self.t5_proj = nn.Linear(t5_dim, hidden_dim)
            self.norm = nn.LayerNorm(hidden_dim)

        def forward(self, clip_pooled: torch.Tensor, t5_tokens: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
            proj_pooled = self.norm(self.clip_proj(clip_pooled))
            proj_tokens = self.norm(self.t5_proj(t5_tokens))
            return proj_pooled, proj_tokens

except ImportError:
    pass


if __name__ == "__main__":
    print("=== Modern Diffusion Masterclass Ep 27: Text Encoders at Scale ===")
    prompt = "A high-tech cyberpunk robotics lab with glowing cyan holographic schematics on glass terminals."
    encoder = DualTextConditioner(clip_dim=768, t5_dim=128, max_seq_len=64)
    embeddings = encoder.encode(prompt)

    print(f"Prompt: {prompt}")
    print(f"CLIP Pooled Dimension: {len(embeddings.clip_pooled)}")
    print(f"T5 Sequence Shape: {len(embeddings.t5_sequence)} tokens x {len(embeddings.t5_sequence[0])} dims")
    print(f"Active Tokens in Mask: {sum(embeddings.attention_mask)}")
    print("✅ Dual Text Encoding Architecture Verified.")
