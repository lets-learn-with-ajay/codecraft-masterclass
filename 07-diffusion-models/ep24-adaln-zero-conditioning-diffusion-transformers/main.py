"""Adaptive Layer Normalization (adaLN-Zero) for Diffusion Transformers.
Codecraft Masterclass: Diffusion Models Ep 24
"""
from __future__ import annotations
import math
from typing import List, Tuple

# Phase 1: Timestep & Class Conditioning Embedding Projection
def get_sinusoidal_timestep_embedding(timesteps: List[float], embed_dim: int) -> List[List[float]]:
    """Generates sinusoidal timestep embeddings for diffusion steps."""
    half_dim = embed_dim // 2
    emb_factor = math.log(10000.0) / (half_dim - 1)
    frequencies = [math.exp(-i * emb_factor) for i in range(half_dim)]
    
    embeddings: List[List[float]] = []
    for t in timesteps:
        vec: List[float] = []
        for freq in frequencies:
            arg = t * freq
            vec.append(math.sin(arg))
            vec.append(math.cos(arg))
        embeddings.append(vec)
    return embeddings


# Phase 2: Adaptive LayerNorm Modulation Parameter Regression (adaLN)
def modulate_features(
    normed_features: List[List[float]],
    scale_shift: Tuple[List[float], List[float]]
) -> List[List[float]]:
    """Modulates normalized features using scale (gamma) and shift (beta).
    Formula: x_mod = x_norm * (1 + gamma) + beta
    """
    gamma, beta = scale_shift
    dim = len(gamma)
    modulated: List[List[float]] = []
    
    for row in normed_features:
        mod_row = [row[i] * (1.0 + gamma[i]) + beta[i] for i in range(dim)]
        modulated.append(mod_row)
        
    return modulated


# Phase 3: Zero-Initialized Gated Residual Connection (adaLN-Zero)
def apply_adaln_zero_gate(
    residual: List[List[float]],
    branch_output: List[List[float]],
    alpha_gate: List[float]
) -> List[List[float]]:
    """Applies dimension-wise gating parameter alpha to block output before addition.
    Formula: out = residual + alpha * branch_output
    Note: At initialization, alpha = 0.0 -> out = residual (Identity mapping).
    """
    dim = len(alpha_gate)
    out: List[List[float]] = []
    
    for r_row, b_row in zip(residual, branch_output):
        out_row = [r_row[i] + alpha_gate[i] * b_row[i] for i in range(dim)]
        out.append(out_row)
        
    return out


def main():
    print("=== Diffusion Masterclass Ep 24: Adaptive LayerNorm (adaLN-Zero) ===")
    
    hidden_dim = 8
    seq_len = 4
    
    # 1. Timestep conditioning
    timesteps = [100.0, 500.0, 999.0]
    t_emb = get_sinusoidal_timestep_embedding(timesteps, hidden_dim)
    print(f"Computed Timestep Embeddings: {len(t_emb)} steps x {len(t_emb[0])} dims")
    print(f"Sample t=100 Embedding: {[round(v, 4) for v in t_emb[0][:4]]}")
    
    # 2. Mock normalized tokens
    tokens = [
        [0.5, -0.2, 1.1, -0.8, 0.3, -0.1, 0.9, -0.4],
        [0.1, -0.5, 0.8, -0.2, 0.4, -0.3, 0.6, -0.1],
        [-0.3, 0.7, -0.4, 0.9, -0.2, 0.5, -0.1, 0.8],
        [0.2, -0.1, 0.5, -0.6, 0.1, -0.4, 0.3, -0.2],
    ]
    
    # Scale (gamma) and Shift (beta) regressed from conditioning
    gamma = [0.10, -0.05, 0.20, -0.15, 0.08, -0.04, 0.12, -0.06]
    beta = [0.02, 0.01, -0.03, 0.04, -0.01, 0.02, -0.02, 0.01]
    
    modulated = modulate_features(tokens, (gamma, beta))
    print(f"\nModulated Feature Token 0: {[round(v, 4) for v in modulated[0][:4]]}")
    
    # 3. Verify zero-init identity preservation (alpha = 0)
    zero_alpha = [0.0] * hidden_dim
    branch_output = [[10.0] * hidden_dim for _ in range(seq_len)]
    initial_residual_out = apply_adaln_zero_gate(tokens, branch_output, zero_alpha)
    
    assert initial_residual_out == tokens, "Zero-init gate must strictly preserve identity!"
    print("✅ Identity Mapping Verified: alpha=0 strictly outputs unmodified residual.")
    
    # 4. Trained gate (alpha > 0)
    trained_alpha = [0.25] * hidden_dim
    trained_out = apply_adaln_zero_gate(tokens, branch_output, trained_alpha)
    expected_val = round(tokens[0][0] + 0.25 * 10.0, 4)
    assert round(trained_out[0][0], 4) == expected_val
    print(f"✅ Gated Output Verified: Token 0, Dim 0 = {round(trained_out[0][0], 4)} (expected {expected_val})")
    
    print("\n✅ Ep 24 adaLN-Zero Conditioning Architecture successfully verified!")


if __name__ == "__main__":
    main()
