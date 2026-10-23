# Episode 28: Image-to-Image & Inpainting: Masked Latent Blending & Noise Injection at Timestep t

![Difficulty: INTERMEDIATE](https://img.shields.io/badge/Difficulty-INTERMEDIATE-a855f7?style=for-the-badge)
![Track: Generative Deep Learning](https://img.shields.io/badge/Track-Generative_Deep_Learning-38bdf8?style=for-the-badge)
[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch_Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@letslearnwithajay)

> **Series**: [Deep Learning & Generative Diffusion Models Masterclass](../README.md)  
> **Narrator**: Microsoft Brian Natural (US Male • `en-US-BrianMultilingualNeural`)  
> **Duration Target**: 30+ Minutes (Full Production Deep Dive)

---

## 📌 Architectural Overview

Modifying existing visual assets. Forward noising source images to intermediate timestep t_start, conditioning diffusion on partial noise, and implementing inpainting with binary masks, latent blending, and dedicated 9-channel inpainting models.

---

## 💡 Key Architectural Takeaways

- Image-to-image injects noise up to timestep t = S * T, allowing the reverse process to retain underlying composition
- Inpainting blends unmasked latents at each reverse step, forcing generated content to harmonize with existing boundaries
- Dedicated inpainting backbones concatenate the binary mask and masked image latents directly into input channels

---

## 🚀 How to Run the Code

```bash
# Navigate to this episode directory
cd codecraft-masterclass/07-diffusion-models/ep28-image-to-image-inpainting-latent-blending

# Execute PyTorch model validation
python model.py
```

---

## 🏷️ Search Tags

`#imagetoimagediffusionpytorch` `#diffusioninpaintingmaskedlatents` `#latentblendinginpainting` `#img2imgstrengthparametermath`
