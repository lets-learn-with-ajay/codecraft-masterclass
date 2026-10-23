import torch
import math

class VarianceScheduleEngine:
    def __init__(self, num_timesteps: int = 1000, schedule_type: str = 'cosine'):
        self.num_timesteps = num_timesteps
        
        if schedule_type == 'linear':
            self.betas = torch.linspace(1e-4, 0.02, num_timesteps)
        elif schedule_type == 'cosine':
            s = 0.008
            steps = num_timesteps + 1
            t = torch.linspace(0, num_timesteps, steps)
            alphas_cumprod = torch.cos(((t / num_timesteps) + s) / (1 + s) * math.pi * 0.5) ** 2
            alphas_cumprod = alphas_cumprod / alphas_cumprod[0]
            betas = 1 - (alphas_cumprod[1:] / alphas_cumprod[:-1])
            self.betas = torch.clamp(betas, 0.0, 0.999)
        else:
            raise ValueError(f'Unsupported schedule: {schedule_type}')
            
        # Pre-compute all cumulative tensors for O(1) training dispatch
        self.alphas = 1.0 - self.betas
        self.alphas_cumprod = torch.cumprod(self.alphas, dim=0)
        self.sqrt_alphas_cumprod = torch.sqrt(self.alphas_cumprod)
        self.sqrt_one_minus_alphas_cumprod = torch.sqrt(1.0 - self.alphas_cumprod)
        self.log_snr = torch.log(self.alphas_cumprod / (1.0 - self.alphas_cumprod))

    def q_sample(self, x_0: torch.Tensor, t: torch.Tensor, noise: torch.Tensor = None) -> torch.Tensor:
        if noise is None:
            noise = torch.randn_like(x_0)
        sqrt_alpha_bar = self.sqrt_alphas_cumprod[t].view(-1, 1, 1, 1)
        sqrt_one_minus_alpha_bar = self.sqrt_one_minus_alphas_cumprod[t].view(-1, 1, 1, 1)
        return sqrt_alpha_bar * x_0 + sqrt_one_minus_alpha_bar * noise

# Test the Engine
engine = VarianceScheduleEngine(num_timesteps=1000, schedule_type='cosine')
dummy_images = torch.randn(16, 3, 64, 64)  # Batch of 16 images
random_timesteps = torch.randint(0, 1000, (16,))
noisy_latents = engine.q_sample(dummy_images, random_timesteps)
assert noisy_latents.shape == dummy_images.shape
print(f'Engine initialized: {engine.num_timesteps} steps. q_sample output verified: {noisy_latents.shape}')
