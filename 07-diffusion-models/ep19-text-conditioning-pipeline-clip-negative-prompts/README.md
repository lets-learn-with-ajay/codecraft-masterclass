# Episode 19: Text Conditioning Pipeline: Tokenization, CLIP Encoders, Pooled Vectors & Negative Prompts

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

End-to-end prompt processing pipeline. Byte-Pair Encoding (BPE) tokenization, 77-token sequence limits, pooled text vectors vs hidden states, and the mathematics of negative prompts in Classifier-Free Guidance.

---

## 💡 Key Architectural Takeaways

- CLIP tokenizers pad or truncate text to 77 tokens, mapping words into 768-dimensional contextual embedding vectors
- Negative prompts replace the empty unconditional string in CFG, repelling the reverse trajectory from unwanted features
- Extrapolating away from negative prompt latents eliminates artifacts, blurriness, and bad anatomy

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep19-text-conditioning-pipeline-clip-negative-prompts

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#CLIPtextencoderstablediffusion` `#negativepromptmathematicsCFG` `#77tokenlimitBPE` `#pooledtextprojectiondiffusion`
