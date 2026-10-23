# Episode 08: Multi-Head Spatial Self-Attention in U-Net: QKV Projections & Receptive Fields

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Overcoming the local receptive field bottleneck of pure convolutions. Injecting Multi-Head Self-Attention blocks into low-resolution U-Net bottleneck layers. Computing QKV projections, attention matrices, and residual scaling in PyTorch.

---

## 💡 Key Architectural Takeaways

- Convolutions only capture local spatial correlations; self-attention provides global O(N^2) cross-pixel context
- Applying attention at 16x16 and 8x8 spatial resolutions avoids quadratic memory explosion while capturing global composition
- Pre-layer normalization and residual connections prevent vanishing gradients across multi-head attention blocks

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep08-multihead-spatial-self-attention-unet

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#spatialselfattentionUNetpytorch` `#multiheadattentiondiffusion` `#QKVprojectionsdiffusionbottleneck` `#receptivefieldselfattention`
