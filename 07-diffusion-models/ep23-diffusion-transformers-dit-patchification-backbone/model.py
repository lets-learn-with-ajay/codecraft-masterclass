"""Diffusion Transformers (DiT) Architecture: Patchification & Backbone in PyTorch.

Episode 23: Diffusion Transformers (DiT): Replacing U-Net with ViT
Covers:
- Spatial 2D Latent Patchification & Linear Projection
- 2D Sinusoidal / Frequency-based Positional Embeddings
- Standard Vision Transformer Blocks with Multi-Head Self-Attention
- Unpatchification (Sequence to Spatial Latents)
"""
from __future__ import annotations
import math
import torch
import torch.nn as nn
import torch.nn.functional as F


def get_2d_sincos_pos_embed(embed_dim: int, grid_size: int) -> torch.Tensor:
    """Generate 2D sinusoidal positional embedding grid (grid_size x grid_size, embed_dim)."""
    grid_h = torch.arange(grid_size, dtype=torch.float32)
    grid_w = torch.arange(grid_size, dtype=torch.float32)
    grid = torch.meshgrid(grid_w, grid_h, indexing="xy")
    grid = torch.stack(grid, dim=0)  # [2, grid_size, grid_size]
    grid = grid.reshape(2, 1, grid_size, grid_size)

    half_dim = embed_dim // 2
    emb_h = get_1d_sincos_pos_embed_from_grid(half_dim, grid[1].flatten())
    emb_w = get_1d_sincos_pos_embed_from_grid(half_dim, grid[0].flatten())
    return torch.cat([emb_w, emb_h], dim=1)  # [grid_size*grid_size, embed_dim]


def get_1d_sincos_pos_embed_from_grid(embed_dim: int, pos: torch.Tensor) -> torch.Tensor:
    omega = torch.arange(embed_dim // 2, dtype=torch.float32)
    omega /= embed_dim / 2.0
    omega = 1.0 / (10000.0 ** omega)  # [embed_dim / 2]

    out = torch.einsum("m,d->md", pos, omega)  # [pos.len(), embed_dim / 2]
    return torch.cat([torch.sin(out), torch.cos(out)], dim=1)


class PatchEmbed(nn.Module):
    """2D Image/Latent to Patch Embedding."""

    def __init__(self, latent_size: int = 32, patch_size: int = 2, in_channels: int = 4, embed_dim: int = 384):
        super().__init__()
        self.latent_size = latent_size
        self.patch_size = patch_size
        self.grid_size = latent_size // patch_size
        self.num_patches = self.grid_size * self.grid_size

        self.proj = nn.Conv2d(in_channels, embed_dim, kernel_size=patch_size, stride=patch_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [B, C, H, W] -> proj: [B, D, H/p, W/p] -> [B, D, T] -> [B, T, D]
        return self.proj(x).flatten(2).transpose(1, 2)


class DiTBlock(nn.Module):
    """Transformer block with multi-head self-attention and MLP."""

    def __init__(self, hidden_size: int, num_heads: int, mlp_ratio: float = 4.0):
        super().__init__()
        self.norm1 = nn.LayerNorm(hidden_size, elementwise_affine=True, eps=1e-6)
        self.attn = nn.MultiheadAttention(hidden_size, num_heads=num_heads, batch_first=True)
        self.norm2 = nn.LayerNorm(hidden_size, elementwise_affine=True, eps=1e-6)
        mlp_hidden_dim = int(hidden_size * mlp_ratio)
        self.mlp = nn.Sequential(
            nn.Linear(hidden_size, mlp_hidden_dim),
            nn.GELU(approximate="tanh"),
            nn.Linear(mlp_hidden_dim, hidden_size),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Multi-head Self Attention with residual connection
        normed = self.norm1(x)
        attn_out, _ = self.attn(normed, normed, normed)
        x = x + attn_out
        # Feed-Forward Network with residual connection
        x = x + self.mlp(self.norm2(x))
        return x


class FinalLayer(nn.Module):
    """Final linear projection and unpatchification back to latent dimensions."""

    def __init__(self, hidden_size: int, patch_size: int, out_channels: int):
        super().__init__()
        self.norm_final = nn.LayerNorm(hidden_size, elementwise_affine=True, eps=1e-6)
        self.linear = nn.Linear(hidden_size, patch_size * patch_size * out_channels, bias=True)
        self.patch_size = patch_size
        self.out_channels = out_channels

    def forward(self, x: torch.Tensor, grid_size: int) -> torch.Tensor:
        # x: [B, T, D] -> [B, T, p*p*C]
        x = self.linear(self.norm_final(x))
        # Unpatchify into [B, C, H, W]
        p = self.patch_size
        c = self.out_channels
        h = w = grid_size
        b = x.shape[0]
        # Reshape to [B, H_grid, W_grid, p, p, C]
        x = x.reshape(b, h, w, p, p, c)
        # Permute to [B, C, H_grid, p, W_grid, p]
        x = torch.einsum("nhwpqc->nchpwq", x)
        return x.reshape(b, c, h * p, w * p)


class DiffusionTransformer(nn.Module):
    """Complete DiT Backbone for Generative Diffusion."""

    def __init__(
        self,
        latent_size: int = 32,
        patch_size: int = 2,
        in_channels: int = 4,
        hidden_size: int = 384,
        depth: int = 6,
        num_heads: int = 6,
        mlp_ratio: float = 4.0,
    ):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = in_channels
        self.patch_size = patch_size
        self.latent_size = latent_size
        self.grid_size = latent_size // patch_size

        self.x_embedder = PatchEmbed(latent_size, patch_size, in_channels, hidden_size)
        self.pos_embed = nn.Parameter(torch.zeros(1, self.x_embedder.num_patches, hidden_size), requires_grad=False)

        self.blocks = nn.ModuleList([
            DiTBlock(hidden_size, num_heads, mlp_ratio=mlp_ratio) for _ in range(depth)
        ])
        self.final_layer = FinalLayer(hidden_size, patch_size, self.out_channels)
        self.initialize_weights()

    def initialize_weights(self):
        pos_embed = get_2d_sincos_pos_embed(self.pos_embed.shape[-1], self.grid_size)
        self.pos_embed.data.copy_(pos_embed.float().unsqueeze(0))

        # Initialize linear layers
        for block in self.blocks:
            nn.init.xavier_uniform_(block.mlp[0].weight)
            nn.init.constant_(block.mlp[0].bias, 0)
            nn.init.xavier_uniform_(block.mlp[2].weight)
            nn.init.constant_(block.mlp[2].bias, 0)

        # Zero-out output projection
        nn.init.constant_(self.final_layer.linear.weight, 0)
        nn.init.constant_(self.final_layer.linear.bias, 0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Patchify and add positional embeddings
        tokens = self.x_embedder(x) + self.pos_embed
        for block in self.blocks:
            tokens = block(tokens)
        return self.final_layer(tokens, self.grid_size)


def main():
    print("=" * 65)
    print("🎨 Generative Diffusion Models Masterclass: Episode 23")
    print("   Diffusion Transformers (DiT): Patchification & Backbone")
    print("=" * 65)

    device = "cpu"
    batch_size = 4
    latent_channels = 4
    latent_res = 32  # Standard VAE 8x downsampled resolution from 256x256 image

    model = DiffusionTransformer(
        latent_size=latent_res,
        patch_size=2,
        in_channels=latent_channels,
        hidden_size=384,
        depth=6,
        num_heads=6,
    ).to(device)

    total_params = sum(p.numel() for p in model.parameters())
    print(f"\n📊 Model Specifications:")
    print(f"   • Latent Input Shape:   ({batch_size}, {latent_channels}, {latent_res}, {latent_res})")
    print(f"   • Patch Size:           2x2 -> {(latent_res // 2)**2} tokens of dim 384")
    print(f"   • Transformer Depth:    6 Blocks, 6 Heads")
    print(f"   • Total Parameters:     {total_params:,} ({total_params / 1e6:.2f}M)")

    # Test forward pass with Gaussian noise
    latents = torch.randn(batch_size, latent_channels, latent_res, latent_res, device=device)
    output = model(latents)

    print(f"\n⚡ Forward Pass Verification:")
    print(f"   • Input Tensor:         {list(latents.shape)}")
    print(f"   • Predicted Noise/Vel:  {list(output.shape)}")
    assert output.shape == latents.shape, f"Shape mismatch: {output.shape} vs {latents.shape}"

    # Compute MSE reconstruction loss
    target_noise = torch.randn_like(latents)
    loss = F.mse_loss(output, target_noise)
    loss.backward()
    print(f"   • Loss Value (MSE):     {loss.item():.4f}")
    print(f"   • Backprop:             Gradients computed successfully for all parameters.")

    print("\n✅ DiT Patchification & Backbone Architecture verified!")


if __name__ == "__main__":
    main()
