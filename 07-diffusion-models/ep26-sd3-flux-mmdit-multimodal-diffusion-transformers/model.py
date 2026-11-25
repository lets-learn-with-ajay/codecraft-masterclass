"""PyTorch MMDiT Reference Implementation (SD3 & Flux.1).
Codecraft Masterclass: Diffusion Models Ep 26
"""
import torch
import torch.nn as nn
from typing import Tuple


class DoubleStreamMMDiTBlock(nn.Module):
    """MMDiT Double-Stream Block (Esser et al., 2024).

    Maintains separate self-attention projections and MLPs for image and text streams.
    """
    def __init__(self, dim: int = 1536, num_heads: int = 24):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = dim // num_heads

        # Image stream projections
        self.img_norm = nn.LayerNorm(dim, elementwise_affine=False, eps=1e-6)
        self.img_qkv = nn.Linear(dim, 3 * dim)
        self.img_mlp = nn.Sequential(
            nn.Linear(dim, 4 * dim),
            nn.GELU(approximate="tanh"),
            nn.Linear(4 * dim, dim),
        )

        # Text stream projections
        self.txt_norm = nn.LayerNorm(dim, elementwise_affine=False, eps=1e-6)
        self.txt_qkv = nn.Linear(dim, 3 * dim)
        self.txt_mlp = nn.Sequential(
            nn.Linear(dim, 4 * dim),
            nn.GELU(approximate="tanh"),
            nn.Linear(4 * dim, dim),
        )

        self.img_proj = nn.Linear(dim, dim)
        self.txt_proj = nn.Linear(dim, dim)

    def forward(
        self, img: torch.Tensor, txt: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        b, n_img, d = img.shape
        _, n_txt, _ = txt.shape

        # Normalize
        norm_img = self.img_norm(img)
        norm_txt = self.txt_norm(txt)

        # Separate QKV
        q_img, k_img, v_img = self.img_qkv(norm_img).chunk(3, dim=-1)
        q_txt, k_txt, v_txt = self.txt_qkv(norm_txt).chunk(3, dim=-1)

        # Concatenate for joint multimodal attention
        q = torch.cat([q_img, q_txt], dim=1)
        k = torch.cat([k_img, k_txt], dim=1)
        v = torch.cat([v_img, v_txt], dim=1)

        # Reshape for multi-head attention
        q = q.view(b, -1, self.num_heads, self.head_dim).transpose(1, 2)
        k = k.view(b, -1, self.num_heads, self.head_dim).transpose(1, 2)
        v = v.view(b, -1, self.num_heads, self.head_dim).transpose(1, 2)

        # Scaled dot-product attention
        attn = torch.nn.functional.scaled_dot_product_attention(q, k, v)
        attn = attn.transpose(1, 2).reshape(b, -1, d)

        # Split back into image and text streams
        attn_img, attn_txt = attn.split([n_img, n_txt], dim=1)

        # Apply output projections and residual connections
        img = img + self.img_proj(attn_img)
        txt = txt + self.txt_proj(attn_txt)

        # Independent Feedforward Networks
        img = img + self.img_mlp(self.img_norm(img))
        txt = txt + self.txt_mlp(self.txt_norm(txt))

        return img, txt


class SingleStreamMMDiTBlock(nn.Module):
    """MMDiT Single-Stream Block (Flux.1 / SD3 late layers).

    Concatenates visual and text tokens into a unified sequence.
    """
    def __init__(self, dim: int = 1536, num_heads: int = 24):
        super().__init__()
        self.norm = nn.LayerNorm(dim, elementwise_affine=False, eps=1e-6)
        self.qkv = nn.Linear(dim, 3 * dim)
        self.proj = nn.Linear(dim, dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, 4 * dim),
            nn.GELU(approximate="tanh"),
            nn.Linear(4 * dim, dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        b, seq_len, d = x.shape
        norm_x = self.norm(x)
        q, k, v = self.qkv(norm_x).chunk(3, dim=-1)

        attn = torch.nn.functional.scaled_dot_product_attention(
            q.view(b, seq_len, 24, -1).transpose(1, 2),
            k.view(b, seq_len, 24, -1).transpose(1, 2),
            v.view(b, seq_len, 24, -1).transpose(1, 2),
        )
        attn = attn.transpose(1, 2).reshape(b, seq_len, d)
        x = x + self.proj(attn)
        x = x + self.mlp(self.norm(x))
        return x
