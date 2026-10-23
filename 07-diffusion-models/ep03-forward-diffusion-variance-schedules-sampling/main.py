import torch
import torch.nn as nn
from typing import Optional, Tuple

class ForwardDiffusionEngine(nn.Module):
    """Production-grade forward diffusion module supporting linear & cosine schedules."""
    def __init__(self, schedule_type: str = 'cosine', timesteps: int = 1000):
        super().__init__()
        self.timesteps = timesteps
        self.schedule_type = schedule_type.lower()
        
        if self.schedule_type == 'linear':
            sched = LinearVarianceSchedule(timesteps=timesteps)
        elif self.schedule_type == 'cosine':
            sched = CosineVarianceSchedule(timesteps=timesteps)
        else:
            raise ValueError(f"Unsupported schedule: {schedule_type}")
            
        # Register all variance tensors as module buffers
        self.register_buffer('betas', sched.betas)
        self.register_buffer('alphas', sched.alphas)
        self.register_buffer('alpha_bars', sched.alpha_bars)
        self.register_buffer('sqrt_alpha_bars', sched.sqrt_alpha_bars)
        self.register_buffer('sqrt_one_minus_alpha_bars', sched.sqrt_one_minus_alpha_bars)

    def q_sample(
        self,
        x_0: torch.Tensor,
        t: torch.Tensor,
        noise: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Applies closed-form forward diffusion to batch x_0 at timesteps t."""
        if noise is None:
            noise = torch.randn_like(x_0)
            
        # Broadcast coefficients from [B] to [B, 1, 1, 1]
        sqrt_ab = self.sqrt_alpha_bars[t].view(-1, 1, 1, 1)
        sqrt_1m_ab = self.sqrt_one_minus_alpha_bars[t].view(-1, 1, 1, 1)
        
        x_t = sqrt_ab * x_0 + sqrt_1m_ab * noise
        return x_t, noise
