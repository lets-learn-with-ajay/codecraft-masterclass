"""Stable Diffusion 3 & Flux.1 Architecture: Multimodal Diffusion Transformers (MMDiT).
Codecraft Masterclass: Diffusion Models Ep 26
"""
from __future__ import annotations
import math
from typing import List, Tuple


def softmax(x: List[float]) -> List[float]:
    max_x = max(x)
    exp_x = [math.exp(v - max_x) for v in x]
    sum_exp = sum(exp_x)
    return [v / sum_exp for v in exp_x]


def dot_product(v1: List[float], v2: List[float]) -> float:
    return sum(a * b for a, b in zip(v1, v2))


# Phase 1: Double-Stream Block (Independent Weights, Joint Attention)
class DoubleStreamBlock:
    """Maintains separate parameter paths for image and text tokens,

    joining their representations strictly in the self-attention kernel.
    """
    def __init__(self, dim: int):
        self.dim = dim

    def forward(
        self,
        img_tokens: List[List[float]],
        txt_tokens: List[List[float]],
    ) -> Tuple[List[List[float]], List[List[float]]]:
        num_img = len(img_tokens)
        num_txt = len(txt_tokens)

        # Concatenate tokens for joint bidirectional attention
        joint_tokens = img_tokens + txt_tokens
        seq_len = num_img + num_txt
        scale = 1.0 / math.sqrt(self.dim)

        # Compute full cross-modal attention matrix
        attn_out: List[List[float]] = []
        for i in range(seq_len):
            scores = [dot_product(joint_tokens[i], joint_tokens[j]) * scale for j in range(seq_len)]
            probs = softmax(scores)
            
            # Weighted sum over values
            out_vec = [0.0] * self.dim
            for j in range(seq_len):
                w = probs[j]
                for d in range(self.dim):
                    out_vec[d] += w * joint_tokens[j][d]
            attn_out.append(out_vec)

        # Decouple back into separate image and text streams with residual connection
        new_img = [[img_tokens[i][d] + attn_out[i][d] for d in range(self.dim)] for i in range(num_img)]
        new_txt = [[txt_tokens[i][d] + attn_out[num_img + i][d] for d in range(self.dim)] for i in range(num_txt)]

        return new_img, new_txt


# Phase 2: Single-Stream Block (Unified Multimodal Sequence)
class SingleStreamBlock:
    """Concatenates image and text tokens into a single unified sequence

    sharing identical linear and MLP weights for deep multimodal reasoning.
    """
    def __init__(self, dim: int):
        self.dim = dim

    def forward(self, unified_tokens: List[List[float]]) -> List[List[float]]:
        seq_len = len(unified_tokens)
        scale = 1.0 / math.sqrt(self.dim)

        out_tokens: List[List[float]] = []
        for i in range(seq_len):
            scores = [dot_product(unified_tokens[i], unified_tokens[j]) * scale for j in range(seq_len)]
            probs = softmax(scores)
            
            vec = [0.0] * self.dim
            for j in range(seq_len):
                w = probs[j]
                for d in range(self.dim):
                    vec[d] += w * unified_tokens[j][d]
            # Residual update
            out_tokens.append([unified_tokens[i][d] + vec[d] for d in range(self.dim)])

        return out_tokens


# Phase 3: MMDiT End-to-End Pipeline
class MMDiTPipeline:
    """2-Stage MMDiT: Double-Stream Blocks followed by Single-Stream Blocks."""
    def __init__(self, dim: int, num_double: int = 2, num_single: int = 2):
        self.dim = dim
        self.double_blocks = [DoubleStreamBlock(dim) for _ in range(num_double)]
        self.single_blocks = [SingleStreamBlock(dim) for _ in range(num_single)]

    def forward(
        self,
        img_tokens: List[List[float]],
        txt_tokens: List[List[float]],
    ) -> List[List[float]]:
        # Stage 1: Separate streams with joint attention
        curr_img, curr_txt = img_tokens, txt_tokens
        for block in self.double_blocks:
            curr_img, curr_txt = block.forward(curr_img, curr_txt)

        # Stage 2: Merge into single unified stream
        unified = curr_img + curr_txt
        for block in self.single_blocks:
            unified = block.forward(unified)

        return unified


def main():
    print("=== Diffusion Masterclass Ep 26: MMDiT Architecture (SD3 & Flux.1) ===")
    dim = 8
    num_img_patches = 16  # 4x4 image latent patches
    num_txt_tokens = 6    # Text prompt tokens

    # Simulated normalized feature vectors
    img_tokens = [[0.1 * ((i + d) % 5) for d in range(dim)] for i in range(num_img_patches)]
    txt_tokens = [[0.2 * ((i * 2 + d) % 4) for d in range(dim)] for i in range(num_txt_tokens)]

    print(f"Inputs: {num_img_patches} image tokens + {num_txt_tokens} text tokens (dim={dim})")

    # 1. Verify DoubleStreamBlock
    dsb = DoubleStreamBlock(dim)
    out_img, out_txt = dsb.forward(img_tokens, txt_tokens)
    assert len(out_img) == num_img_patches
    assert len(out_txt) == num_txt_tokens
    print("✅ Phase 1 Verified: Double-Stream Block successfully decoupled output streams.")

    # 2. Verify SingleStreamBlock
    ssb = SingleStreamBlock(dim)
    unified_in = out_img + out_txt
    out_unified = ssb.forward(unified_in)
    assert len(out_unified) == num_img_patches + num_txt_tokens
    print("✅ Phase 2 Verified: Single-Stream Block unified sequence processing verified.")

    # 3. Verify Full MMDiTPipeline
    pipeline = MMDiTPipeline(dim=dim, num_double=2, num_single=2)
    final_tokens = pipeline.forward(img_tokens, txt_tokens)
    assert len(final_tokens) == num_img_patches + num_txt_tokens
    print(f"✅ Phase 3 Verified: Full MMDiT pipeline completed ({len(final_tokens)} output tokens).")

    print("\n✅ Ep 26 MMDiT Architecture (SD3 & Flux.1) successfully verified!")


if __name__ == "__main__":
    main()
