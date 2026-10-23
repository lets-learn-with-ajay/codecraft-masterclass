# Episode 15: Classifier-Free Guidance (CFG): Joint Training, Dropout Conditioning & Contrast Amplification

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

The breakthrough that powers all modern diffusion models (Ho & Salimans). Eliminating external classifiers via joint training with conditioning dropout. The CFG formula: eps_guided = eps_uncond + w * (eps_cond - eps_uncond). Implementing CFG in PyTorch.

---

## 💡 Key Architectural Takeaways

- CFG trains a single model for both conditional and unconditional generation by randomly dropping conditioning (10-20%)
- During sampling, the model extrapolates in the direction of the conditioning vector using guidance scale w > 1.0
- CFG completely eliminates the need for external classifiers and forms the foundation of Stable Diffusion, Midjourney, and Flux

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep15-classifier-free-guidance-cfg-dropout-amplification

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#classifierfreeguidancetutorialpytorch` `#CFGdiffusionformula` `#conditioningdropoutdiffusion` `#guidancescalewexplained`
