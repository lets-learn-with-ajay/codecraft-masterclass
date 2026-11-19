"""Diffusion Transformers (DiT): Replacing U-Net with ViT — Patchification & Backbone.
Codecraft Masterclass: Diffusion Models Ep 23
"""
from __future__ import annotations
import math
from typing import List, Tuple

# Phase 1: Spatial 2D Latent Patchification & Linear Projection
def patchify_2d(
    spatial_tensor: List[List[List[float]]],
    patch_size: int = 2
) -> Tuple[List[List[float]], int, int]:
    """Divides (C, H, W) spatial latent tensor into flattened (T, C * p * p) sequence tokens.
    
    Args:
        spatial_tensor: 3D tensor of shape [channels, height, width]
        patch_size: Square patch spatial dimension (p)
        
    Returns:
        tokens: Flattened sequence tokens of shape [T, C * patch_size * patch_size]
        grid_h: Number of vertical patch tokens
        grid_w: Number of horizontal patch tokens
    """
    c = len(spatial_tensor)
    h = len(spatial_tensor[0])
    w = len(spatial_tensor[0][0])
    assert h % patch_size == 0 and w % patch_size == 0, "Dimensions must be divisible by patch size"
    
    grid_h = h // patch_size
    grid_w = w // patch_size
    tokens: List[List[float]] = []
    
    for gh in range(grid_h):
        for gw in range(grid_w):
            patch_vec: List[float] = []
            for ch in range(c):
                for py in range(patch_size):
                    for px in range(patch_size):
                        y = gh * patch_size + py
                        x = gw * patch_size + px
                        patch_vec.append(spatial_tensor[ch][y][x])
            tokens.append(patch_vec)
            
    return tokens, grid_h, grid_w


# Phase 2: 2D Sinusoidal Frequency Positional Embeddings
def get_2d_sincos_pos_embed(embed_dim: int, grid_h: int, grid_w: int) -> List[List[float]]:
    """Calculates 2D frequency positional embeddings for spatial grid tokens."""
    half_dim = embed_dim // 2
    quarter_dim = half_dim // 2
    omega = [1.0 / (10000.0 ** (2 * i / half_dim)) for i in range(quarter_dim)]
    
    pos_embeddings: List[List[float]] = []
    for y in range(grid_h):
        for x in range(grid_w):
            emb: List[float] = []
            # Horizontal (x) frequency encoding
            for freq in omega:
                emb.append(math.sin(x * freq))
                emb.append(math.cos(x * freq))
            # Vertical (y) frequency encoding
            for freq in omega:
                emb.append(math.sin(y * freq))
                emb.append(math.cos(y * freq))
            # Pad if needed to match exact embed_dim
            while len(emb) < embed_dim:
                emb.append(0.0)
            pos_embeddings.append(emb)
            
    return pos_embeddings


# Phase 3: Spatial Unpatchification & Reconstruction
def unpatchify_2d(
    tokens: List[List[float]],
    channels: int,
    grid_h: int,
    grid_w: int,
    patch_size: int = 2
) -> List[List[List[float]]]:
    """Reconstructs (C, H, W) spatial latent tensor from sequence tokens."""
    h = grid_h * patch_size
    w = grid_w * patch_size
    output = [[[0.0 for _ in range(w)] for _ in range(h)] for _ in range(channels)]
    
    token_idx = 0
    for gh in range(grid_h):
        for gw in range(grid_w):
            patch_vec = tokens[token_idx]
            vec_idx = 0
            for ch in range(channels):
                for py in range(patch_size):
                    for px in range(patch_size):
                        y = gh * patch_size + py
                        x = gw * patch_size + px
                        output[ch][y][x] = patch_vec[vec_idx]
                        vec_idx += 1
            token_idx += 1
            
    return output


def main():
    print("=== Diffusion Masterclass Ep 23: Diffusion Transformers (DiT) Patchification ===")
    
    # 4-channel VAE latent representation of size 8x8 (scaled for verification)
    channels = 4
    height, width = 8, 8
    patch_size = 2
    
    # Synthetic latent map
    latents = [
        [[float(c * 100 + y * 10 + x) for x in range(width)] for y in range(height)]
        for c in range(channels)
    ]
    
    # 1. Patchify
    tokens, gh, gw = patchify_2d(latents, patch_size=patch_size)
    num_tokens = len(tokens)
    patch_dim = len(tokens[0])
    print(f"Latent Spatial Shape: ({channels}, {height}, {width})")
    print(f"Grid Layout: {gh}x{gw} patches ({patch_size}x{patch_size})")
    print(f"Sequence Tokens: {num_tokens} tokens of dimension {patch_dim}")
    
    # 2. 2D Sinusoidal Positional Embeddings
    embed_dim = 16
    pos_embed = get_2d_sincos_pos_embed(embed_dim, gh, gw)
    print(f"Positional Embeddings Shape: ({len(pos_embed)}, {len(pos_embed[0])})")
    print(f"Sample Token 0 Positional Embedding: {[round(v, 4) for v in pos_embed[0][:4]]}")
    
    # 3. Unpatchify & Lossless Verification
    reconstructed = unpatchify_2d(tokens, channels, gh, gw, patch_size=patch_size)
    
    # Verify lossless roundtrip
    max_diff = 0.0
    for c in range(channels):
        for y in range(height):
            for x in range(width):
                diff = abs(latents[c][y][x] - reconstructed[c][y][x])
                if diff > max_diff:
                    max_diff = diff
                    
    print(f"Reconstruction Max Absolute Error: {max_diff:.8f}")
    assert max_diff < 1e-6, "Lossless patchification invariant violated!"
    print("\n✅ Ep 23 DiT Patchification & 2D Positional Backbone successfully verified!")


if __name__ == "__main__":
    main()
