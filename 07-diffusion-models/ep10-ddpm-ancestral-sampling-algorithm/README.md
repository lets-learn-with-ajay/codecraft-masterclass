# Episode 10: DDPM Ancestral Sampling Algorithm: Reverse SDE Discretization & First Image Generation

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Executing the reverse generation process. Iterating backwards from t = T down to t = 0. Subtracting predicted noise, re-scaling by variance schedules, adding controlled Langevin noise, and generating our first synthetic images.

---

## 💡 Key Architectural Takeaways

- Ancestral sampling starts with pure random noise x_T ~ N(0, I) and iteratively subtracts predicted noise
- At each step t > 1, controlled Gaussian noise sigma_t * z is re-injected to prevent trajectory collapse
- At t = 0, no noise is injected, yielding the clean deterministic reconstructed sample x_0

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep10-ddpm-ancestral-sampling-algorithm

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#DDPMsamplingalgorithmpytorch` `#ancestralsamplingreversediffusion` `#generateimagesdiffusionfromscratch` `#langevindynamicsnoiseinjection`
