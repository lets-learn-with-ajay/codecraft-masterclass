# Episode 21: Rectified Flow & Linear Interpolation: Straight Paths Between Noise and Data

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

The modern foundation of Flux and Stable Diffusion 3 (Liu et al.). Replacing curved Brownian diffusion paths with straight linear interpolation: x_t = (1-t)x_0 + t*x_1. Proving why straight trajectories minimize transport cost and simulation error.

---

## 💡 Key Architectural Takeaways

- Rectified Flow connects noise x_0 ~ N(0, I) and data x_1 along straight trajectories with constant velocity
- Straight trajectories have zero curvature, eliminating discretization errors and enabling ultra-fast Euler solving
- Reflow algorithms straighten trajectories further by pairing generated samples with initial noise vectors

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep21-rectified-flow-linear-interpolation-straight-paths

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#rectifiedflowtutorial` `#straightpathsflowmatching` `#x_t=(1-t)x_0+t*x_1` `#rectifiedflowvsdiffusion`
