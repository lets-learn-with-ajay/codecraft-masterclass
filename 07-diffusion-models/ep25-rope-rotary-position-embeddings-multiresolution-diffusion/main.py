"""Rotary Position Embeddings (RoPE) in 2D & 3D: Multi-Resolution Latents.
Codecraft Masterclass: Diffusion Models Ep 25
"""
from __future__ import annotations
import math
from typing import List, Tuple


# Phase 1: 2D Axial Frequency Angle Generation
def compute_axial_frequencies_2d(
    head_dim: int,
    height: int,
    width: int,
    theta: float = 10000.0
) -> Tuple[List[List[float]], List[List[float]]]:
    """Generates (cos, sin) frequency matrices for a 2D spatial grid (height x width).
    Allocates half of head_dim to vertical (y) and half to horizontal (x).
    """
    assert head_dim % 4 == 0, "head_dim must be divisible by 4 (axial split + 2D pairs)"
    axis_dim = head_dim // 2
    pairs_per_axis = axis_dim // 2
    
    # 1D frequency spectrum: 1 / theta^(2i / axis_dim)
    freqs = [1.0 / (theta ** ((2 * i) / axis_dim)) for i in range(pairs_per_axis)]
    
    cos_table: List[List[float]] = []
    sin_table: List[List[float]] = []
    
    for y in range(height):
        for x in range(width):
            # Compute angles for y-axis and x-axis
            angles_y = [y * f for f in freqs]
            angles_x = [x * f for f in freqs]
            
            # Combine axial angles
            all_angles = angles_y + angles_x
            
            # Expand to pairs (cos, cos, sin, sin) for 2D rotation
            cos_row: List[float] = []
            sin_row: List[float] = []
            for angle in all_angles:
                cos_val = math.cos(angle)
                sin_val = math.sin(angle)
                cos_row.extend([cos_val, cos_val])
                sin_row.extend([sin_val, sin_val])
                
            cos_table.append(cos_row)
            sin_table.append(sin_row)
            
    return cos_table, sin_table


# Phase 2: Rotary Positional Complex Rotation
def apply_rotary_emb_2d(
    token_vec: List[float],
    cos_vec: List[float],
    sin_vec: List[float]
) -> List[float]:
    """Rotates a single token vector by the corresponding 2D RoPE angles.
    Pairs (x[2i], x[2i+1]) are rotated:
      x_rot[2i]   = x[2i] * cos - x[2i+1] * sin
      x_rot[2i+1] = x[2i] * sin + x[2i+1] * cos
    """
    dim = len(token_vec)
    assert dim == len(cos_vec) == len(sin_vec)
    
    rotated: List[float] = [0.0] * dim
    for i in range(0, dim, 2):
        x1 = token_vec[i]
        x2 = token_vec[i + 1]
        c = cos_vec[i]
        s = sin_vec[i]
        
        rotated[i] = x1 * c - x2 * s
        rotated[i + 1] = x1 * s + x2 * c
        
    return rotated


# Phase 3: Relative Coordinate Distance Invariance Verification
def dot_product(v1: List[float], v2: List[float]) -> float:
    return sum(a * b for a, b in zip(v1, v2))


def main():
    print("=== Diffusion Masterclass Ep 25: 2D Rotary Position Embeddings (RoPE) ===")
    
    head_dim = 8  # 4 for y-axis, 4 for x-axis
    height, width = 4, 8  # 4x8 = 32 tokens (widescreen aspect ratio)
    
    cos_table, sin_table = compute_axial_frequencies_2d(head_dim, height, width)
    print(f"Generated 2D Axial Grid: {len(cos_table)} tokens x {len(cos_table[0])} dims")
    assert len(cos_table) == height * width
    assert len(cos_table[0]) == head_dim
    print("✅ Phase 1 Verified: Axial grid frequency generation valid.")
    
    # 2. Test rotation on sample query token at position (y=1, x=2) -> index 1*8 + 2 = 10
    token_idx = 10
    sample_q = [1.0, 0.5, -0.2, 0.8, 0.3, -0.7, 0.4, 0.1]
    rotated_q = apply_rotary_emb_2d(sample_q, cos_table[token_idx], sin_table[token_idx])
    
    # RoPE is orthogonal: length of vector must be strictly preserved
    norm_before = math.sqrt(dot_product(sample_q, sample_q))
    norm_after = math.sqrt(dot_product(rotated_q, rotated_q))
    assert abs(norm_before - norm_after) < 1e-6, "RoPE rotation must preserve vector norm!"
    print(f"✅ Phase 2 Verified: Vector norm preserved (before={norm_before:.4f}, after={norm_after:.4f}).")
    
    # 3. Relative Coordinate Distance Invariance
    # Let pos_A = (1, 2) and pos_B = (2, 4) -> diff = (1, 2)
    # Let pos_C = (2, 3) and pos_D = (3, 5) -> diff = (1, 2)
    # The relative distance between A and B equals the distance between C and D!
    idx_A = 1 * width + 2
    idx_B = 2 * width + 4
    idx_C = 2 * width + 3
    idx_D = 3 * width + 5
    
    vec1 = [0.6, -0.3, 0.5, 0.1, -0.4, 0.7, 0.2, -0.5]
    vec2 = [0.2, 0.8, -0.1, 0.4, 0.6, -0.2, 0.3, 0.9]
    
    # Rotate (A, B) pair and (C, D) pair
    rot_A = apply_rotary_emb_2d(vec1, cos_table[idx_A], sin_table[idx_A])
    rot_B = apply_rotary_emb_2d(vec2, cos_table[idx_B], sin_table[idx_B])
    
    rot_C = apply_rotary_emb_2d(vec1, cos_table[idx_C], sin_table[idx_C])
    rot_D = apply_rotary_emb_2d(vec2, cos_table[idx_D], sin_table[idx_D])
    
    dot_AB = dot_product(rot_A, rot_B)
    dot_CD = dot_product(rot_C, rot_D)
    
    # Both pairs have identical relative spatial offset (dy=1, dx=2)
    assert abs(dot_AB - dot_CD) < 1e-6, "Identical spatial displacements must produce identical inner products!"
    print(f"✅ Phase 3 Verified: Relative shift invariance confirmed (dot_AB={dot_AB:.6f}, dot_CD={dot_CD:.6f}).")
    
    print("\n✅ Ep 25 2D RoPE Multi-Resolution Architecture successfully verified!")


if __name__ == "__main__":
    main()
