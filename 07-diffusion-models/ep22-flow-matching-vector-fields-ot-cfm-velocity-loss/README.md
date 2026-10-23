# Episode 22: Flow Matching vs Diffusion: Vector Field Regression, OT-CFM & Velocity Loss

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Lipman et al. Flow Matching framework. Learning probability paths via Continuous Normalizing Flows (CNF). Conditional Flow Matching (CFM), Optimal Transport Flow Matching (OT-CFM), and training neural networks to predict velocity v_t(x).

---

## 💡 Key Architectural Takeaways

- Flow Matching frames generative modeling as learning a time-dependent velocity vector field v_theta(x, t)
- Optimal Transport CFM minimizes kinetic energy by pairing noise and data with shortest Euclidean distances
- Loss function is simple regression: L_CFM = E[||v_theta(x_t, t) - (x_1 - x_0)||^2], directly estimating constant velocity

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep22-flow-matching-vector-fields-ot-cfm-velocity-loss

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#flowmatchingtutorialpytorch` `#optimaltransportflowmatchingOT-CFM` `#velocitylossflowmatching` `#conditionalflowmatchinglipman`
