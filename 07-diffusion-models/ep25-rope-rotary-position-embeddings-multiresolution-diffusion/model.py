"""PyTorch Reference: 2D & 3D Rotary Position Embeddings (RoPE) for DiT.
Episode 25: Rotary Position Embeddings (RoPE) in Diffusion
"""
import math
import torch
import torch.nn as nn


def build_axial_frequencies_2d(
    dim: int,
    height: int,
    width: int,
    theta: float = 10000.0,
    device: torch.device = None
) -> tuple[torch.Tensor, torch.Tensor]:
    """Generates 2D rotary position frequencies for multi-resolution feature maps."""
    assert dim % 4 == 0, "Head dimension must be divisible by 4 for 2D RoPE."
    axis_dim = dim // 2
    
    freq_indices = torch.arange(0, axis_dim, 2, dtype=torch.float32, device=device)
    freqs = 1.0 / (theta ** (freq_indices / axis_dim))
    
    y_coords = torch.arange(height, dtype=torch.float32, device=device)
    x_coords = torch.arange(width, dtype=torch.float32, device=device)
    
    angles_y = torch.outer(y_coords, freqs).unsqueeze(1).expand(height, width, -1)
    angles_x = torch.outer(x_coords, freqs).unsqueeze(0).expand(height, width, -1)
    
    angles = torch.cat([angles_y, angles_x], dim=-1).reshape(height * width, -1)
    
    cos = torch.cos(angles).repeat_interleave(2, dim=-1)
    sin = torch.sin(angles).repeat_interleave(2, dim=-1)
    return cos, sin


def rotate_half(x: torch.Tensor) -> torch.Tensor:
    x1 = x[..., 0::2]
    x2 = x[..., 1::2]
    return torch.stack((-x2, x1), dim=-1).flatten(-2)


def apply_rotary_emb_2d(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
    cos = cos.unsqueeze(0).unsqueeze(1)
    sin = sin.unsqueeze(0).unsqueeze(1)
    return (x * cos) + (rotate_half(x) * sin)


class MultiResolutionRoPEAttention(nn.Module):
    def __init__(self, hidden_dim: int = 256, num_heads: int = 4):
        super().__init__()
        assert hidden_dim % num_heads == 0
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.head_dim = hidden_dim // num_heads
        
        self.qkv_proj = nn.Linear(hidden_dim, 3 * hidden_dim, bias=False)
        self.out_proj = nn.Linear(hidden_dim, hidden_dim, bias=False)

    def forward(self, x: torch.Tensor, height: int, width: int) -> torch.Tensor:
        B, N, C = x.shape
        assert N == height * width
        
        qkv = self.qkv_proj(x).chunk(3, dim=-1)
        q = qkv[0].view(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        k = qkv[1].view(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        v = qkv[2].view(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        
        cos, sin = build_axial_frequencies_2d(self.head_dim, height, width, device=x.device)
        q_rot = apply_rotary_emb_2d(q, cos, sin)
        k_rot = apply_rotary_emb_2d(k, cos, sin)
        
        scale = 1.0 / math.sqrt(self.head_dim)
        attn_scores = torch.matmul(q_rot, k_rot.transpose(-2, -1)) * scale
        attn_probs = torch.softmax(attn_scores, dim=-1)
        
        out = torch.matmul(attn_probs, v).transpose(1, 2).contiguous().view(B, N, C)
        return self.out_proj(out)
