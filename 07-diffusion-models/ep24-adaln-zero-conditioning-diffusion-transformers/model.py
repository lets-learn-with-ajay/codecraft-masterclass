"""PyTorch Reference: Adaptive Layer Normalization (adaLN-Zero) for DiT.
Episode 24: Adaptive Layer Normalization (adaLN-Zero)
"""
import torch
import torch.nn as nn

class AdaLNZeroBlock(nn.Module):
    """Transformer Block with adaLN-Zero modulation for DiT."""
    def __init__(self, hidden_dim: int = 1152, num_heads: int = 16, mlp_ratio: float = 4.0):
        super().__init__()
        self.norm1 = nn.LayerNorm(hidden_dim, elementwise_affine=False, eps=1e-6)
        self.attn = nn.MultiheadAttention(hidden_dim, num_heads=num_heads, batch_first=True)
        self.norm2 = nn.LayerNorm(hidden_dim, elementwise_affine=False, eps=1e-6)
        
        mlp_hidden_dim = int(hidden_dim * mlp_ratio)
        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim, mlp_hidden_dim),
            nn.GELU(approximate="tanh"),
            nn.Linear(mlp_hidden_dim, hidden_dim),
        )
        
        # 6 modulation parameters: (gamma1, beta1, alpha1, gamma2, beta2, alpha2)
        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(),
            nn.Linear(hidden_dim, 6 * hidden_dim, bias=True)
        )
        # Initialize modulation weights to zero (zero-init gate identity preservation)
        nn.init.constant_(self.adaLN_modulation[-1].weight, 0)
        nn.init.constant_(self.adaLN_modulation[-1].bias, 0)

    def forward(self, x: torch.Tensor, c: torch.Tensor) -> torch.Tensor:
        # c: [B, D] conditioning vector (timestep + label embedding)
        mod = self.adaLN_modulation(c).chunk(6, dim=-1)
        shift_msa, scale_msa, gate_msa, shift_mlp, scale_mlp, gate_mlp = [m.unsqueeze(1) for m in mod]
        
        # Self-Attention branch with adaLN modulation & zero-init gate
        normed1 = self.norm1(x) * (1 + scale_msa) + shift_msa
        attn_out, _ = self.attn(normed1, normed1, normed1)
        x = x + gate_msa * attn_out
        
        # Feed-Forward branch with adaLN modulation & zero-init gate
        normed2 = self.norm2(x) * (1 + scale_mlp) + shift_mlp
        mlp_out = self.mlp(normed2)
        x = x + gate_mlp * mlp_out
        return x
