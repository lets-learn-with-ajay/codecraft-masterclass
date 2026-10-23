# Episode 24: Adaptive Layer Normalization (adaLN-Zero): Conditioning DiT on Timesteps & Classes

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

How Diffusion Transformers ingest conditioning information. Comparing Cross-Attention, In-Context conditioning, and Adaptive Layer Normalization (adaLN). Implementing adaLN-Zero with zero-initialized gating layers for stable gradient flow.

---

## 💡 Key Architectural Takeaways

- adaLN regresses scale (gamma), shift (beta), and gate (alpha) parameters directly from conditioning embeddings
- Zero-initializing the gating parameter alpha ensures residual blocks act as identity mappings at training inception
- adaLN-Zero dramatically outperforms standard cross-attention in parameter efficiency and training stability

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep24-adaln-zero-conditioning-diffusion-transformers

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#adaLN-zeroexplainedpytorch` `#adaptivelayernormdiffusiontransformer` `#conditioningDiTtimestepclass` `#zeroinitializationtransformergate`
