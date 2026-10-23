# Episode 05: DDPM from Scratch (Part 1): Reparameterization Trick & Simplified Loss Function

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Implementing Denoising Diffusion Probabilistic Models (Ho et al.). Transitioning from mu-prediction to epsilon-prediction, simplifying the weighted variational loss to MSE, and implementing the loss function in pure PyTorch.

---

## 💡 Key Architectural Takeaways

- Predicting the injected noise epsilon rather than the mean mu significantly stabilizes gradient descent
- The simplified loss L_simple strips complex weighting terms, boosting perceptual sample quality
- MSE loss between actual Gaussian noise epsilon and neural network prediction epsilon_theta(x_t, t)

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep05-ddpm-scratch-epsilon-prediction-loss

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#DDPMfromscratchpytorch` `#epsilonpredictionloss` `#simplifiedlossL_simple` `#Hoetaldiffusionimplementation`
