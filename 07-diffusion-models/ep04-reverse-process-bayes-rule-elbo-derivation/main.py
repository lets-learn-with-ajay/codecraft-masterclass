import torch
import torch.nn as nn

class AnalyticalPosteriorParameters(nn.Module):
    """Computes analytical posterior q(x_{t-1} | x_t, x_0) coefficients."""
    def __init__(self, beta_schedule: torch.Tensor):
        super().__init__()
        self.betas = beta_schedule
        self.alphas = 1.0 - self.betas
        self.alphas_cumprod = torch.cumprod(self.alphas, dim=0)
        # alpha_cumprod_prev with 1.0 prepended for t=0
        self.alphas_cumprod_prev = torch.cat([torch.tensor([1.0]), self.alphas_cumprod[:-1]])
        
        # Posterior variance: beta_tilde_t = beta_t * (1 - alpha_bar_{t-1}) / (1 - alpha_bar_t)
        self.posterior_variance = (
            self.betas * (1.0 - self.alphas_cumprod_prev) / (1.0 - self.alphas_cumprod)
        )
        # Clipped variance for log stability at t=0
        self.posterior_log_variance_clipped = torch.log(
            torch.clamp(self.posterior_variance, min=1e-20)
        )
        
        # Coefficient for x_0: sqrt(alpha_bar_{t-1}) * beta_t / (1 - alpha_bar_t)
        self.posterior_mean_coef1 = (
            torch.sqrt(self.alphas_cumprod_prev) * self.betas / (1.0 - self.alphas_cumprod)
        )
        # Coefficient for x_t: sqrt(alpha_t) * (1 - alpha_bar_{t-1}) / (1 - alpha_bar_t)
        self.posterior_mean_coef2 = (
            torch.sqrt(self.alphas) * (1.0 - self.alphas_cumprod_prev) / (1.0 - self.alphas_cumprod)
        )

    def forward(self, t: torch.Tensor):
        return {
            'var': self.posterior_variance[t],
            'log_var': self.posterior_log_variance_clipped[t],
            'coef_x0': self.posterior_mean_coef1[t],
            'coef_xt': self.posterior_mean_coef2[t]
        }
