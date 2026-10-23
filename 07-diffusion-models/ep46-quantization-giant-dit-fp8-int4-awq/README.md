# Episode 46: Quantization of Giant Diffusion Transformers: FP8 (E4M3/E5M2), INT4 Weight-Only & AWQ

![Difficulty: ADVANCED](https://img.shields.io/badge/Difficulty-ADVANCED-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Running 12B+ parameter models (Flux.1, SD3) on consumer GPUs. Numerical formats: FP8 (E4M3 for weights/activations, E5M2 for gradients), Activation-aware Weight Quantization (AWQ), and tensor RT-LLM dynamic quantization.

---

## 💡 Key Architectural Takeaways

- FP8 (E4M3) preserves dynamic range in attention weights while cutting VRAM usage by 50% on modern Ada/Hopper/Blackwell GPUs
- Activation-aware Weight Quantization (AWQ) protects salient 1% outlier weights to maintain visual fidelity under INT4/INT8
- Reduces memory footprint of 12B DiT models from 24GB down to 12GB, enabling local high-resolution inference

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep46-quantization-giant-dit-fp8-int4-awq

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#FP8quantizationdiffusionmodels` `#quantizeFlux1model` `#AWQactivationawarequantizationDiT` `#run12BdiffusionconsumerGPU`
