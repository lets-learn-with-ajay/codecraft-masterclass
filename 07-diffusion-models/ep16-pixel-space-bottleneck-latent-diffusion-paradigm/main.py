import torch
import torch.nn as nn

class EncoderResBlock(nn.Module):
    '''Convolutional residual block with GroupNorm for AutoencoderKL.'''
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        self.norm1 = nn.GroupNorm(32, in_channels)
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1)
        self.norm2 = nn.GroupNorm(32, out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1)
        self.act = nn.SiLU()
        self.shortcut = nn.Conv2d(in_channels, out_channels, 1) if in_channels != out_channels else nn.Identity()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.conv1(self.act(self.norm1(x)))
        h = self.conv2(self.act(self.norm2(h)))
        return h + self.shortcut(x)

class AutoencoderEncoder(nn.Module):
    '''8x Downsampling Encoder mapping [B, 3, 512, 512] to [B, 8, 64, 64].'''
    def __init__(self, in_channels: int = 3, latent_channels: int = 4):
        super().__init__()
        self.conv_in = nn.Conv2d(in_channels, 64, kernel_size=3, padding=1)
        # Three downsampling stages (factor of 2^3 = 8)
        self.down1 = nn.Sequential(EncoderResBlock(64, 64), nn.Conv2d(64, 64, 3, stride=2, padding=1))
        self.down2 = nn.Sequential(EncoderResBlock(64, 128), nn.Conv2d(128, 128, 3, stride=2, padding=1))
        self.down3 = nn.Sequential(EncoderResBlock(128, 256), nn.Conv2d(256, 256, 3, stride=2, padding=1))
        self.norm_out = nn.GroupNorm(32, 256)
        # Emits mean and log-variance: 2 * latent_channels = 8 channels
        self.conv_out = nn.Conv2d(256, 2 * latent_channels, kernel_size=3, padding=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.conv_in(x)
        h = self.down3(self.down2(self.down1(h)))
        return self.conv_out(nn.functional.silu(self.norm_out(h)))
