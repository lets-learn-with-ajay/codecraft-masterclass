# Episode 45: RLHF for Diffusion: Direct Preference Optimization (Diffusion-DPO) & Score Reweighting

![Difficulty: ADVANCED](https://img.shields.io/badge/Difficulty-ADVANCED-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Aligning generative models with human aesthetics (Wallace et al. 2024). Extending DPO to diffusion: formulating implicit reward models from human preference pairs (winner vs loser images). Deriving Diffusion-DPO loss and fine-tuning DiT backbones.

---

## 💡 Key Architectural Takeaways

- Diffusion-DPO eliminates complex reward model training by directly optimizing the likelihood ratio between winner and loser samples
- Implicit reward formulation aligns generated images with aesthetic quality, photorealism, and prompt faithfulness
- Prevents mode collapse while dramatically boosting human evaluation win rates across benchmark datasets

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep45-rlhf-diffusion-dpo-direct-preference-optimization

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#Diffusion-DPOtutorialpytorch` `#directpreferenceoptimizationdiffusion` `#RLHFforimagegeneration` `#aligndiffusionmodelshumanpreferences`
