# Phase 1: Diffusion Transformer (DiT) 2D Spatial Patchification
import torch
import torch.nn as nn

class DiTPatchEmbed(nn.Module):
    def __init__(self, in_ch: int = 4, hidden_dim: int = 1152, patch_size: int = 2):
        super().__init__()
        self.proj = nn.Conv2d(in_ch, hidden_dim, kernel_size=patch_size, stride=patch_size)

    def forward(self, latent: torch.Tensor) -> torch.Tensor:
        patches = self.proj(latent)
        return patches.flatten(2).transpose(1, 2)

# Phase 2: Adaptive LayerNorm-Zero (adaLN-Zero) Timestep Modulation
class AdaLNZeroBlock(nn.Module):
    def __init__(self, hidden_dim: int = 1152):
        super().__init__()
        self.norm = nn.LayerNorm(hidden_dim, elementwise_affine=False, eps=1e-6)
        self.modulation = nn.Sequential(nn.SiLU(), nn.Linear(hidden_dim, 3 * hidden_dim))
        nn.init.zeros_(self.modulation[-1].weight)
        nn.init.zeros_(self.modulation[-1].bias)

    def forward(self, x: torch.Tensor, cond_vec: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        shift, scale, gate = self.modulation(cond_vec).unsqueeze(1).chunk(3, dim=-1)
        modulated = self.norm(x) * (1.0 + scale) + shift
        return modulated, gate

# Phase 3: Gated Residual Attention & Velocity Prediction Head
def apply_gated_residual(
    residual: torch.Tensor,
    branch_out: torch.Tensor,
    gate: torch.Tensor,
) -> torch.Tensor:
    return residual + gate * branch_out
