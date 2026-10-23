# Episode 30: IP-Adapter & Decoupled Cross-Attention: Image Prompts & Style Transfer Without Retraining

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Conditioning diffusion on images rather than text (Ye et al.). The limitation of text-to-image adapters. Decoupled cross-attention mechanism: separate cross-attention layers for text and image features, merged via weighted summation.

---

## 💡 Key Architectural Takeaways

- Decoupled cross-attention adds a dedicated cross-attention projection for image tokens without interfering with text layers
- CLIP image encoders extract grid and global feature vectors from reference images (faces, styles, textures)
- The output attention maps are combined: Output = Softmax(QK_text^T)V_text + lambda * Softmax(QK_img^T)V_img

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep30-ip-adapter-decoupled-cross-attention-image-prompts

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#IP-Adaptertutorialpytorch` `#decoupledcrossattentiondiffusion` `#imagepromptconditioning` `#styletransferIP-Adapter`
