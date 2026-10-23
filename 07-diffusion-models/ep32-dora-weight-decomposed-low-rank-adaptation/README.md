# Episode 32: DoRA (Weight-Decomposed Low-Rank Adaptation): Magnitude vs Direction Decomposition

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Next-generation parameter-efficient fine-tuning (Liu et al. 2024). Decomposing weight matrices into magnitude vectors and directional matrices: W = m * (W_0 + B*A) / ||W_0 + B*A||. Why DoRA matches full fine-tuning performance in diffusion models.

---

## 💡 Key Architectural Takeaways

- LoRA couples magnitude and direction updates, limiting learning capacity compared to full fine-tuning
- DoRA explicitly decouples weight magnitude (scalar scale) from directional trajectory (low-rank rotation)
- Achieves superior visual fidelity and prompt alignment without increasing the parameter footprint during inference

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep32-dora-weight-decomposed-low-rank-adaptation

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#DoRAtutorialdiffusionmodels` `#weightdecomposedlowrankadaptation` `#DoRAvsLoRAfinetuning` `#magnitudedirectiondecompositionpytorch`
