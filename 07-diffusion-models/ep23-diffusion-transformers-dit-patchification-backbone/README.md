# Episode 23: Diffusion Transformers (DiT): Replacing U-Net with ViT — Patchification & Scaling Laws

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Peebles & Xie Diffusion Transformers (DiT). Why convolutions have reached their scaling limit. Transforming 2D latents into 1D patch tokens, linear patch projection, standard ViT Transformer blocks, and demonstrating compute scaling laws.

---

## 💡 Key Architectural Takeaways

- DiT divides 64x64 latent feature maps into 2x2 or 4x4 spatial patches, flattening them into sequence tokens
- Eliminates inductive bias of convolutions, allowing models to scale cleanly with compute following power laws
- Higher GigaFLOPs DiT models consistently achieve lower Frechet Inception Distance (FID) and higher sample fidelity

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep23-diffusion-transformers-dit-patchification-backbone

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#diffusiontransformersDiTtutorial` `#replaceUNetwithtransformerdiffusion` `#patchificationvisiontransformerpytorch` `#DiTscalinglawsgenerativeAI`
