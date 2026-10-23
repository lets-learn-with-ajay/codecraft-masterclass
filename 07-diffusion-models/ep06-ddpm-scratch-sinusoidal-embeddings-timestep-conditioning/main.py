class MiniConditionedUNet(nn.Module):
    '''Compact, fully functional U-Net with hierarchical time conditioning.'''
    def __init__(self, in_channels: int = 3, out_channels: int = 3, time_dim: int = 128):
        super().__init__()
        self.time_mlp = TimeProjectionMLP(embed_dim=32, target_dim=time_dim)
        self.conv_in = nn.Conv2d(in_channels, 64, kernel_size=3, padding=1)
        self.down1 = ResBlockTime(64, 64, time_dim)
        self.pool1 = nn.MaxPool2d(2)
        self.down2 = ResBlockTime(64, 128, time_dim)
        self.pool2 = nn.MaxPool2d(2)
        self.mid = ResBlockTime(128, 128, time_dim)
        self.up2 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.up_block2 = ResBlockTime(128, 64, time_dim)
        self.up1 = nn.ConvTranspose2d(64, 64, kernel_size=2, stride=2)
        self.up_block1 = ResBlockTime(128, 64, time_dim)
        self.conv_out = nn.Conv2d(64, out_channels, kernel_size=3, padding=1)

    def forward(self, x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        t_emb = self.time_mlp(t)
        x1 = self.conv_in(x)
        d1 = self.down1(x1, t_emb)
        d2 = self.down2(self.pool1(d1), t_emb)
        m = self.mid(self.pool2(d2), t_emb)
        u2 = self.up2(m)
        u2 = self.up_block2(torch.cat([u2, d2], dim=1), t_emb)
        u1 = self.up1(u2)
        u1 = self.up_block1(torch.cat([u1, d1], dim=1), t_emb)
        return self.conv_out(u1)
