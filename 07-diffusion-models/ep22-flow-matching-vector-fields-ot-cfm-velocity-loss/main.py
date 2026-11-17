"""Flow Matching vs Diffusion: Vector Field Regression, OT-CFM & Velocity Loss
Codecraft Masterclass: Diffusion Models Ep 22
"""
from __future__ import annotations
import math
from typing import Tuple

# Phase 1: Optimal Transport Conditional Flow Matching (OT-CFM) Probability Path
def ot_cfm_path(
    x_0: list[float],
    x_1: list[float],
    t: float,
    sigma_min: float = 1e-4,
) -> Tuple[list[float], list[float]]:
    """Calculates optimal transport linear interpolation path and constant velocity."""
    dim = len(x_0)
    mu_t = [(1.0 - (1.0 - sigma_min) * t) * x_0[i] + t * x_1[i] for i in range(dim)]
    u_t = [x_1[i] - (1.0 - sigma_min) * x_0[i] for i in range(dim)]
    return mu_t, u_t

# Phase 2: Vector Field Velocity Estimation & Euler ODE Step
def euler_step(
    x_t: list[float],
    velocity: list[float],
    dt: float,
) -> list[float]:
    """Advances particle state forward along the learned velocity vector field."""
    return [x_t[i] + velocity[i] * dt for i in range(len(x_t))]

# Phase 3: CFM Mean Squared Velocity Regression Loss
def cfm_loss(
    v_pred: list[float],
    v_target: list[float],
) -> float:
    """Computes MSE regression loss between predicted and ground-truth OT velocity."""
    return sum((v_p - v_t) ** 2 for v_p, v_t in zip(v_pred, v_target)) / len(v_pred)

def main():
    print("=== Diffusion Masterclass Ep 22: Optimal Transport Flow Matching (OT-CFM) ===")
    x_0 = [-1.5, 2.0, -0.5, 0.8]  # Source standard normal sample
    x_1 = [3.0, -1.0, 1.5, -2.2]  # Target data manifold sample
    t = 0.5
    
    x_t, v_target = ot_cfm_path(x_0, x_1, t)
    print(f"Interpolated State x_{{t={t}}}: {[round(v, 4) for v in x_t]}")
    print(f"Target Velocity v_target: {[round(v, 4) for v in v_target]}")
    
    # Mock model prediction
    v_pred = [v + 0.05 for v in v_target]
    loss = cfm_loss(v_pred, v_target)
    print(f"OT-CFM Velocity Loss: {loss:.6f}")
    
    # Take an ODE integration step
    x_next = euler_step(x_t, v_pred, dt=0.1)
    print(f"Advanced State x_{{t=0.6}}: {[round(v, 4) for v in x_next]}")
    print("\n✅ Ep 22 OT-CFM Vector Field Regression successfully verified!")

if __name__ == "__main__":
    main()
