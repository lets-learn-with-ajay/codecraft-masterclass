# Episode 34: Latent Consistency Models (LCM) & Consistency Distillation: Real-Time 2–4 Step Synthesis

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Breaking the iterative barrier (Luo et al.). Enforcing the self-consistency property along Probability Flow ODE trajectories: f(x_t, t) = f(x_t', t') = x_0. Distilling multi-step teachers into 2-to-4 step generators, and LCM-LoRA plug-and-play modules.

---

## 💡 Key Architectural Takeaways

- Consistency models map any point along an ODE trajectory directly to its initial trajectory origin in a single step
- Consistency distillation trains a student model using a pre-calculated solver trajectory from a teacher model
- Enables photorealistic image generation in just 2 to 4 sampling steps, enabling sub-200ms real-time generation

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep34-latent-consistency-models-lcm-distillation-few-steps

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#latentconsistencymodelsLCMtutorial` `#consistencydistillationdiffusion` `#2stepimagegenerationLCM` `#LCM-LoRAfastinference`
