# Phase 1: Karras Sigma Discretization Schedule (rho = 7.0)
import torch

def build_karras_sigmas(
    num_steps: int = 20,
    sigma_min: float = 0.002,
    sigma_max: float = 80.0,
    rho: float = 7.0,
) -> torch.Tensor:
    ramp = torch.linspace(0.0, 1.0, num_steps)
    min_inv_rho = sigma_min ** (1.0 / rho)
    max_inv_rho = sigma_max ** (1.0 / rho)
    sigmas = (max_inv_rho + ramp * (min_inv_rho - max_inv_rho)) ** rho
    return torch.cat([sigmas, torch.zeros(1)])

# Phase 2: Second-Order Heun Predictor-Corrector ODE Solver Step
@torch.no_grad()
def heun_step(
    model,
    x: torch.Tensor,
    sigma_cur: torch.Tensor,
    sigma_next: torch.Tensor,
    cond: torch.Tensor,
) -> torch.Tensor:
    denoised_cur = model(x, sigma_cur, cond)
    d_cur = (x - denoised_cur) / sigma_cur.clamp(min=1e-6)
    dt = sigma_next - sigma_cur
    x_euler = x + d_cur * dt
    if float(sigma_next) == 0.0:
        return x_euler
    denoised_next = model(x_euler, sigma_next, cond)
    d_next = (x_euler - denoised_next) / sigma_next.clamp(min=1e-6)
    return x + 0.5 * (d_cur + d_next) * dt

# Phase 3: DPM-Solver++ 2M Second-Order Multistep ODE Integration
def dpm_solver_2m_multistep(
    x: torch.Tensor,
    model_prev: torch.Tensor,
    model_curr: torch.Tensor,
    sigma_prev: float,
    sigma_curr: float,
    sigma_next: float,
) -> torch.Tensor:
    import math
    lambda_prev = -math.log(max(sigma_prev, 1e-6))
    lambda_curr = -math.log(max(sigma_curr, 1e-6))
    lambda_next = -math.log(max(sigma_next, 1e-6))
    h = lambda_next - lambda_curr
    h_prev = lambda_curr - lambda_prev
    r = h_prev / (h if abs(h) > 1e-6 else 1e-6)
    d = (1.0 + 1.0 / (2.0 * r)) * model_curr - (1.0 / (2.0 * r)) * model_prev
    return (sigma_next / sigma_curr) * x - math.expm1(-h) * d
