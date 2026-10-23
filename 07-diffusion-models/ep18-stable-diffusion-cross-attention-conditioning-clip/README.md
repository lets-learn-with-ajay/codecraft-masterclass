# Episode 18: Stable Diffusion Architecture Deconstructed: Cross-Attention on CLIP Text Embeddings

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Full architectural dissection of Stable Diffusion. Spatial Transformer blocks inside U-Net, injecting text conditioning via Cross-Attention: Q from latent features, K and V from CLIP ViT-L/14 text token embeddings. Implementing Cross-Attention in PyTorch.

---

## 💡 Key Architectural Takeaways

- Spatial Transformer blocks replace standard convolutions at intermediate resolutions to fuse multimodal context
- Cross-attention uses spatial image features as Queries and text encoder token embeddings as Keys and Values
- Enables individual image regions to attend to specific prompt words (e.g., 'red hair', 'cyberpunk jacket')

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep18-stable-diffusion-cross-attention-conditioning-clip

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#stablediffusioncrossattentionpytorch` `#CLIPtextembeddingconditioning` `#spatialtransformerblockunet` `#howstablediffusionunderstandsprompts`
