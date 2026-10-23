# Episode 11: DDIM (Denoising Diffusion Implicit Models): Non-Markovian Acceleration (1000 -> 50 Steps)

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Solving the 1000-step sampling bottleneck. Song et al. DDIM formulation: Non-Markovian forward process sharing identical marginals with DDPM. Deterministic sampling trajectory, sub-sampling timesteps, and accelerating generation by 20x.

---

## 💡 Key Architectural Takeaways

- DDIM generalizes DDPM to non-Markovian processes while retaining the exact same trained U-Net weights
- Setting eta = 0 yields completely deterministic ODE sampling where a latent noise code maps to a unique image
- Enables accelerating sampling from 1,000 steps down to 50 or 20 steps with negligible loss in perceptual quality

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep11-ddim-deterministic-sampling-acceleration

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#DDIMexplainedpytorch` `#denoisingdiffusionimplicitmodelstutorial` `#fastdiffusionsamplingDDIM` `#deterministicdiffusiontrajectory`
