# Episode 17: Variational Autoencoders (VAE) for Latents: LPIPS Loss, KL Penalty & Scaling Factors

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Building the perceptual compression engine. Training AutoencoderKL with perceptual loss (LPIPS), PatchGAN discriminator loss, and KL divergence regularization. Measuring latent variance and deriving the crucial scaling factor (0.18215).

---

## 💡 Key Architectural Takeaways

- The VAE encoder maps 512x512x3 images into 64x64x4 latent representations, compressing spatial volume by 48x
- LPIPS perceptual loss preserves fine textures and sharp edges that MSE blur would otherwise smooth out
- The latent scaling factor normalizes latent channel variance to 1.0, matching standard Gaussian prior assumptions

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep17-variational-autoencoders-vae-lpips-latent-scaling

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#AutoencoderKLstablediffusion` `#LPIPSperceptuallossVAE` `#latentscalingfactor0.18215` `#trainVAEforlatentdiffusion`
