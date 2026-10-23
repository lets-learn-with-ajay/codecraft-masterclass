import torch
import torch.nn as nn

class AutoencoderKL(nn.Module):
    '''Production-grade AutoencoderKL module with built-in latent scaling.'''
    def __init__(
        self,
        in_channels: int = 3,
        out_channels: int = 3,
        latent_channels: int = 4,
        scaling_factor: float = 0.18215
    ):
        super().__init__()
        self.scaling_factor = scaling_factor
        # In a full model, encoder downsamples 8x and outputs 2 * latent_channels
        self.encoder_conv = nn.Sequential(
            nn.Conv2d(in_channels, 64, kernel_size=3, stride=2, padding=1),  # /2
            nn.SiLU(),
            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),          # /4
            nn.SiLU(),
            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),         # /8
            nn.SiLU(),
            nn.Conv2d(256, 2 * latent_channels, kernel_size=3, padding=1)    # 8 channels
        )
        # Decoder mirrors encoder upsampling 8x
        self.decoder_conv = nn.Sequential(
            nn.ConvTranspose2d(latent_channels, 128, kernel_size=4, stride=2, padding=1), # *2
            nn.SiLU(),
            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),             # *4
            nn.SiLU(),
            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),              # *8
            nn.SiLU(),
            nn.Conv2d(32, out_channels, kernel_size=3, padding=1)
        )

    def encode(self, x: torch.Tensor, sample_posterior: bool = True) -> torch.Tensor:
        moments = self.encoder_conv(x)
        mean, logvar = torch.chunk(moments, 2, dim=1)
        if not sample_posterior:
            return mean * self.scaling_factor
        std = torch.exp(0.5 * torch.clamp(logvar, -30.0, 20.0))
        z = mean + std * torch.randn_like(mean)
        return z * self.scaling_factor

    def decode(self, z_scaled: torch.Tensor) -> torch.Tensor:
        # Unscale before decoding
        z = z_scaled / self.scaling_factor
        return self.decoder_conv(z)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        moments = self.encoder_conv(x)
        mean, logvar = torch.chunk(moments, 2, dim=1)
        std = torch.exp(0.5 * torch.clamp(logvar, -30.0, 20.0))
        z = mean + std * torch.randn_like(mean)
        recon = self.decoder_conv(z)
        return recon, mean, logvar

# Verification Harness
vae = AutoencoderKL(in_channels=3, out_channels=3, latent_channels=4)
sample_img = torch.randn(2, 3, 256, 256)
latents = vae.encode(sample_img)
reconstructed = vae.decode(latents)
print(f'Full VAE Pipeline: Input {sample_img.shape} -> Latents {latents.shape} -> Recon {reconstructed.shape}')
