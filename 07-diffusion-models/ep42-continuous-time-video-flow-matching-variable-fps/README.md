# Episode 42: Continuous-Time Video Flow Matching: Velocity Fields & Variable Frame Rates

![Difficulty: ADVANCED](https://img.shields.io/badge/Difficulty-ADVANCED-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Applying Flow Matching to 4D spacetime tensors. Defining continuous velocity vector fields for video volumes, training with Optimal Transport paths, and conditioning models on continuous frame rate (FPS) and duration embeddings.

---

## 💡 Key Architectural Takeaways

- Flow Matching in 4D spacetime models fluid motion as straight trajectories between Gaussian video noise and true video latents
- Conditioning on continuous FPS embeddings allows a single model to synthesize 12fps, 24fps, and 60fps video dynamically
- Reduces inference steps while eliminating temporal jitter and flickering common in traditional diffusion samplers

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep42-continuous-time-video-flow-matching-variable-fps

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#continuoustimevideoflowmatching` `#variableframeratevideodiffusion` `#4Dspacetimevelocityfield` `#flowmatchingvideotutorialpytorch`
