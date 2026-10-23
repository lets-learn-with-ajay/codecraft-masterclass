# Episode 12: Continuous-Time Score-Based Modeling: Langevin Dynamics & Score Matching

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Unifying diffusion with score-based generative modeling (Song & Ermon). Defining the Stein score function grad_x log p(x), Denoising Score Matching, Langevin dynamics sampling, and why scores eliminate partition function estimation.

---

## 💡 Key Architectural Takeaways

- The score function grad_x log p(x) points toward high-density regions of the data distribution
- Taking gradients of the log probability eliminates the intractable normalizing partition function Z
- DDPM noise prediction epsilon_theta is mathematically equivalent to scaled negative score estimation

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep12-continuous-time-score-based-modeling-langevin

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#scorebasedgenerativemodeling` `#steinscorefunctiondeeplearning` `#langevindynamicsscorematching` `#denoisingscorematchingsongermon`
