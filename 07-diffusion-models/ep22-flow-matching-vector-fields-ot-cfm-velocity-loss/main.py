# Phase 1: Flow Matching Linear Optimal Transport Trajectory
import torch

def sample_flow_matching_path(x_0: torch.Tensor, x_1: torch.Tensor, t: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    t_expand = t.view(-1, 1, 1, 1)
    x_t = (1.0 - t_expand) * x_0 + t_expand * x_1
    target_v = x_1 - x_0
    return x_t, target_v

# Phase 2: Flow Field Velocity Network Forward Pass
def predict_velocity(velocity_net, x_t: torch.Tensor, t: torch.Tensor, cond: torch.Tensor) -> torch.Tensor:
    return velocity_net(x_t, t, cond)

# Phase 3: Rectified Flow Straight-Line Velocity Field Regression
def compute_rectified_flow_loss(
    velocity_net,
    x_data: torch.Tensor,
    cond: torch.Tensor,
) -> torch.Tensor:
    x_noise = torch.randn_like(x_data)
    t = torch.rand(x_data.size(0), device=x_data.device)
    x_t, target_v = sample_flow_matching_path(x_noise, x_data, t)
    pred_v = predict_velocity(velocity_net, x_t, t, cond)
    return torch.mean((pred_v - target_v) ** 2)
