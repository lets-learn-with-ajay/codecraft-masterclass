# Episode 31: LoRA (Low-Rank Adaptation) for Diffusion: Rank Decomposition & Weight Merging

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Efficient parameter fine-tuning (Hu et al.). Mathematical rank decomposition: Delta W = B * A with rank r << d. Injecting LoRA into Attention QKV projections, memory savings, alpha scaling, and dynamically merging LoRAs into base model weights.

---

## 💡 Key Architectural Takeaways

- LoRA freezes pretrained weights W_0 and trains two low-rank matrices B (d x r) and A (r x k), reducing parameters by 99%
- Scaling factor alpha / r stabilizes gradient updates across varying rank hyperparameter choices
- At inference time, Delta W can be directly added into base model weights with zero added latency or memory overhead

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep31-lora-low-rank-adaptation-diffusion-fine-tuning

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#LoRAfordiffusionmodelspytorch` `#lowrankadaptationrankdecomposition` `#trainLoRAstablediffusion` `#mergeLoRAweightszerolatency`
