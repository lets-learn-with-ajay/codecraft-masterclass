# Episode 13: SDEs & ODEs in Generative Modeling: Variance Preserving vs Exploding & Probability Flow

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

The grand unified theory of diffusion (Song et al. 2021). Formulating diffusion as Stochastic Differential Equations (SDEs): Variance Preserving (VP) and Variance Exploding (VE). Deriving the deterministic Probability Flow ODE and exact log-likelihood computation.

---

## 💡 Key Architectural Takeaways

- Continuous-time SDEs describe the infinite-step limit of forward perturbation: dx = f(x,t)dt + g(t)dw
- Every diffusion SDE has an associated Probability Flow ODE that shares identical marginal probability densities
- The Probability Flow ODE enables exact log-likelihood computation via instantaneous change-of-variables formula

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep13-sdes-odes-probability-flow-song-formulation

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#scoreSDEdiffusiontutorial` `#variancepreservingvsexplodingSDE` `#probabilityflowODEpytorch` `#exactlikelihooddiffusioncontinuoustime`
