# Episode 36: Spatiotemporal Video Diffusion: Expanding 2D Latents to 3D Volumes & Temporal Attention

![Difficulty: ADVANCED](https://img.shields.io/badge/Difficulty-ADVANCED-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Transitioning from images to video. Structuring video as 5D tensors (B x C x T x H x W). Factorized spatiotemporal architectures: interleaving spatial attention blocks (frame structure) with temporal attention blocks (motion coherence).

---

## 💡 Key Architectural Takeaways

- Video generation extends latent spatial grids across time: latents become 5D tensors (B x C x T x H x W)
- Factorized space-time attention computes spatial attention within frames and temporal attention across identical pixel coordinates
- Decoupling spatial and temporal operations avoids catastrophic O(T^2 * H^2 * W^2) full 3D attention complexity

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep36-spatiotemporal-video-diffusion-3d-latents-temporal-attention

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#videodiffusionmodelstutorial` `#spatiotemporalattentionpytorch` `#temporalconvolutionvideodiffusion` `#5Dtensorvideogeneration`
