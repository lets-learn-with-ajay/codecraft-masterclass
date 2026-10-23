# Episode 14: Classifier Guidance: Steering Diffusion with External Pretrained Classifiers

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Controlling the generation trajectory. Dhariwal & Nichol classifier guidance: using the gradient of a noise-conditioned classifier grad_x log p(y|x_t) to steer reverse sampling toward specific class labels. Analyzing fidelity vs diversity trade-offs.

---

## 💡 Key Architectural Takeaways

- Classifier guidance adds the gradient of class probability to the score function during sampling
- Higher guidance scale s dramatically increases image fidelity and class alignment at the cost of diversity
- Requires training a specialized noise-aware classifier on noisy latents at all timesteps t

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep14-classifier-guidance-score-gradients

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#classifierguidancediffusionmodels` `#steerdiffusionpretrainedclassifier` `#scoregradientsclassifierguidance` `#dhariwalnicholdiffusionguidance`
