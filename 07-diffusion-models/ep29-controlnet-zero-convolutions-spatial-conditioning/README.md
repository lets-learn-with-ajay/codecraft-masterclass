# Episode 29: ControlNet Architecture: Zero-Convolution Cloned Encoders & Spatial Conditioning

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Zhang & Agrawala ControlNet. Locking base diffusion weights and training a cloned encoder with zero-initialized 1x1 convolutions. Conditioning generation on Canny edges, depth maps, surface normals, and OpenPose skeletons.

---

## 💡 Key Architectural Takeaways

- ControlNet duplicates the encoding layers of the diffusion model while keeping original backbone parameters frozen
- Zero-convolutions are initialized with weights and bias set to 0, ensuring zero disturbance to the model at step 0
- Provides pixel-perfect spatial composition control without retraining the multi-billion parameter foundation model

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep29-controlnet-zero-convolutions-spatial-conditioning

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#ControlNetarchitecturetutorialpytorch` `#zeroconvolutionControlNetmath` `#spatialconditioningdiffusion` `#traincontrolnetfromscratch`
