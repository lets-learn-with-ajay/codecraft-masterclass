# Episode 35: Adversarial Diffusion Distillation (ADD / SDXL-Turbo): 1-Step Real-Time Inference

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Sauer et al. (Stability AI). Combining Score Distillation Sampling (SDS) with adversarial discriminator objectives. Training a student model to output photorealistic samples in a single forward pass without CFG, eliminating sampling loops entirely.

---

## 💡 Key Architectural Takeaways

- Score Distillation loss utilizes a frozen pretrained diffusion teacher to guide student outputs in high-density regions
- An adversarial discriminator loss forces the single-step outputs to remain on the natural image manifold without blur
- Enables true single-step (1-step, 50ms) inference on consumer hardware, transforming diffusion into a real-time engine

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep35-adversarial-diffusion-distillation-add-sdxl-turbo-1step

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#adversarialdiffusiondistillationADD` `#SDXL-Turbo1-stepdiffusion` `#scoredistillationsamplingSDS` `#realtime1-stepimagegeneration`
