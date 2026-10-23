# Episode 06: DDPM from Scratch (Part 2): 2D Sinusoidal Positional Embeddings & Timestep Conditioning

![Difficulty: BASIC](https://img.shields.io/badge/Difficulty-BASIC-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

How neural networks understand time. Implementing Vaswani sinusoidal frequency embeddings for scalar timesteps, MLP projection layers, and broadcasting temporal guidance vectors into convolutional feature maps.

---

## 💡 Key Architectural Takeaways

- Continuous sinusoidal embeddings map scalar discrete timesteps t in [0, T] to high-dimensional frequency representations
- MLP projection blocks expand time embeddings to match channel dimensions of convolutional residual layers
- Feature-wise Linear Modulation (FiLM) modulates activations using scale and shift factors derived from time embeddings

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep06-ddpm-scratch-sinusoidal-embeddings-timestep-conditioning

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#sinusoidaltimestepembeddingspytorch` `#diffusiontimeconditioning` `#temporalembeddingMLP` `#howdiffusionmodelsknowtime`
