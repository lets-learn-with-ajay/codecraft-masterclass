"""
Diffusion Models Masterclass - Episode 28: Image-to-Image & Inpainting
Masked Latent Blending, Noise Injection at Timestep t, and 9-Channel Inpainting Conditioning
"""

import math
import random
import unittest
from dataclasses import dataclass
from typing import List, Tuple, Optional


# ============================================================================
# Phase 1: Image-to-Image Noise Scheduler (Strength Parameter & Timestep t_start)
# ============================================================================

class Img2ImgNoiseScheduler:
    """
    Implements forward noise injection for Image-to-Image generation:
    Given initial clean latent x_0 and strength parameter S in (0.0, 1.0]:
    1. Calculate initial diffusion timestep: t_start = int(S * total_timesteps)
    2. Modulate cumulative variance: alpha_bar_t
    3. Perturb clean latent: x_t = sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * epsilon
    """
    def __init__(self, total_timesteps: int = 1000, beta_start: float = 0.00085, beta_end: float = 0.012):
        self.total_timesteps = total_timesteps
        self.betas = [
            beta_start + i * (beta_end - beta_start) / (total_timesteps - 1)
            for i in range(total_timesteps)
        ]
        self.alphas = [1.0 - b for b in self.betas]
        self.alphas_cumprod = []
        prod = 1.0
        for a in self.alphas:
            prod *= a
            self.alphas_cumprod.append(prod)

    def get_start_timestep(self, strength: float) -> int:
        """Computes t_start based on user transformation strength."""
        clamped = max(0.01, min(1.0, strength))
        t = int(clamped * self.total_timesteps) - 1
        return max(0, min(self.total_timesteps - 1, t))

    def add_noise(
        self,
        clean_latents: List[List[float]],
        t: int,
        noise: Optional[List[List[float]]] = None
    ) -> Tuple[List[List[float]], List[List[float]]]:
        """
        Injects forward Gaussian noise at timestep t.
        Formula: x_t = sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * noise
        """
        rows = len(clean_latents)
        cols = len(clean_latents[0])
        alpha_bar = self.alphas_cumprod[t]
        sqrt_alpha = math.sqrt(alpha_bar)
        sqrt_one_minus_alpha = math.sqrt(1.0 - alpha_bar)

        if noise is None:
            noise = [[random.gauss(0.0, 1.0) for _ in range(cols)] for _ in range(rows)]

        noisy_latents = [
            [
                sqrt_alpha * clean_latents[r][c] + sqrt_one_minus_alpha * noise[r][c]
                for c in range(cols)
            ]
            for r in range(rows)
        ]
        return noisy_latents, noise


# ============================================================================
# Phase 2: Inpainting Masked Latent Blending (RePaint Algorithm)
# ============================================================================

class LatentBlendingInpainter:
    """
    Implements iterative latent blending for inpainting:
    At each reverse diffusion step t:
    1. Sample noise into the unmasked clean image to get x_t_known.
    2. Obtain the denoised candidate from the diffusion model: x_t_unknown.
    3. Composite them using binary mask M (1 = inpaint region, 0 = keep original):
       x_t_blended = (1 - M) * x_t_known + M * x_t_unknown
    """
    def __init__(self, scheduler: Img2ImgNoiseScheduler):
        self.scheduler = scheduler

    def blend_step(
        self,
        clean_latents: List[List[float]],
        predicted_latents: List[List[float]],
        mask: List[List[float]],
        t: int,
        fixed_noise: Optional[List[List[float]]] = None
    ) -> List[List[float]]:
        rows = len(clean_latents)
        cols = len(clean_latents[0])

        # Step 1: Forward diffuse known region to timestep t
        known_noisy, _ = self.scheduler.add_noise(clean_latents, t, noise=fixed_noise)

        # Step 2: Harmonic blend with mask
        blended = []
        for r in range(rows):
            row = []
            for c in range(cols):
                m = mask[r][c]  # 1.0 = generate, 0.0 = retain
                val = (1.0 - m) * known_noisy[r][c] + m * predicted_latents[r][c]
                row.append(val)
            blended.append(row)
        return blended


# ============================================================================
# Phase 3: Dedicated 9-Channel Inpainting Input Conditioning
# ============================================================================

@dataclass
class NineChannelTensor:
    noisy_latents: List[List[List[float]]]      # 4 channels: x_t
    mask_channel: List[List[List[float]]]       # 1 channel: downsampled binary mask
    masked_clean_latents: List[List[List[float]]] # 4 channels: x_0 * (1 - mask)

    def total_channels(self) -> int:
        return (
            len(self.noisy_latents) +
            len(self.mask_channel) +
            len(self.masked_clean_latents)
        )


class DedicatedInpaintingPacker:
    """
    Prepares input tensors for dedicated inpainting models (e.g. SD Inpainting):
    Input dimension: 9 channels = [noisy_latents (4), mask (1), masked_clean (4)]
    Allows the U-Net/DiT to condition directly on surrounding unmasked visual texture.
    """
    @staticmethod
    def pack(
        noisy_latents: List[List[List[float]]],      # shape [4, H, W]
        mask: List[List[float]],                     # shape [H, W]
        clean_latents: List[List[List[float]]]       # shape [4, H, W]
    ) -> NineChannelTensor:
        h = len(mask)
        w = len(mask[0])

        # 1. Mask channel [1, H, W]
        mask_channel = [[row[:] for row in mask]]

        # 2. Masked clean latents [4, H, W]: x_0 * (1 - mask)
        masked_clean = []
        for ch in range(len(clean_latents)):
            ch_data = []
            for r in range(h):
                row = []
                for c in range(w):
                    m = mask[r][c]
                    row.append(clean_latents[ch][r][c] * (1.0 - m))
                ch_data.append(row)
            masked_clean.append(ch_data)

        return NineChannelTensor(
            noisy_latents=noisy_latents,
            mask_channel=mask_channel,
            masked_clean_latents=masked_clean
        )


# ============================================================================
# PyTorch Reference Implementation (when torch is available)
# ============================================================================

try:
    import torch
    import torch.nn as nn

    class PyTorchInpaintingConcat(nn.Module):
        """Standard 9-channel concatenation layer for PyTorch inpainting backbones."""
        def __init__(self, in_channels: int = 9, out_channels: int = 320):
            super().__init__()
            self.input_conv = nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1)

        def forward(self, x_t: torch.Tensor, mask: torch.Tensor, x_0: torch.Tensor) -> torch.Tensor:
            # x_t: [B, 4, H, W], mask: [B, 1, H, W], x_0: [B, 4, H, W]
            masked_clean = x_0 * (1.0 - mask)
            concatenated = torch.cat([x_t, mask, masked_clean], dim=1) # [B, 9, H, W]
            return self.input_conv(concatenated)

except ImportError:
    torch = None


# ============================================================================
# Verification Suite & Self-Checking Unit Tests
# ============================================================================

class TestImageToImageAndInpainting(unittest.TestCase):
    def setUp(self):
        self.scheduler = Img2ImgNoiseScheduler(total_timesteps=1000)
        self.inpainter = LatentBlendingInpainter(self.scheduler)

    def test_img2img_strength_timesteps(self):
        """Validates strength scaling to diffusion start timesteps."""
        self.assertEqual(self.scheduler.get_start_timestep(1.0), 999)
        self.assertEqual(self.scheduler.get_start_timestep(0.5), 499)
        self.assertAlmostEqual(self.scheduler.get_start_timestep(0.2), 199, delta=1)

    def test_forward_noise_injection(self):
        """Verifies forward noise injection preserves dimensions and alters values."""
        clean = [[1.0, 2.0], [3.0, 4.0]]
        noisy, noise = self.scheduler.add_noise(clean, t=500)
        self.assertEqual(len(noisy), 2)
        self.assertEqual(len(noisy[0]), 2)
        # Check that noisy values are not identical to clean
        self.assertNotEqual(clean[0][0], noisy[0][0])

    def test_latent_blending_mask_boundaries(self):
        """Verifies exact adherence to mask boundaries during latent blending."""
        clean = [[10.0, 10.0], [10.0, 10.0]]
        pred = [[-5.0, -5.0], [-5.0, -5.0]]
        # Mask: Top row is known (0.0), bottom row is inpaint target (1.0)
        mask = [[0.0, 0.0], [1.0, 1.0]]
        zero_noise = [[0.0, 0.0], [0.0, 0.0]]

        blended = self.inpainter.blend_step(clean, pred, mask, t=0, fixed_noise=zero_noise)

        # Top row retains known clean latent (scaled by alpha at t=0)
        self.assertAlmostEqual(blended[0][0], 10.0, places=1)
        # Bottom row strictly takes predicted value
        self.assertAlmostEqual(blended[1][0], -5.0, places=2)

    def test_nine_channel_packing(self):
        """Validates dedicated 9-channel tensor construction."""
        h, w = 4, 4
        noisy = [[[1.0] * w for _ in range(h)] for _ in range(4)]
        clean = [[[2.0] * w for _ in range(h)] for _ in range(4)]
        mask = [[1.0 if r >= 2 else 0.0 for _ in range(w)] for r in range(h)]

        packed = DedicatedInpaintingPacker.pack(noisy, mask, clean)
        self.assertEqual(packed.total_channels(), 9)
        # Check unmasked clean value: top half should have 2.0, bottom half 0.0
        self.assertEqual(packed.masked_clean_latents[0][0][0], 2.0)
        self.assertEqual(packed.masked_clean_latents[0][2][0], 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
