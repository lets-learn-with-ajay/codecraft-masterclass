# ⚡ Track: Deep Learning & Generative Diffusion Models Masterclass

> **Domain**: Generative Deep Learning • **Tagline**: Master mathematical foundations, DDPM, Latent Diffusion, Flow Matching, DiT, and Video Generation from scratch

Official YouTube Playlist: [Watch Playlist](https://www.youtube.com/@letslearnwithajay)

## 📚 Episode Navigation & Curriculum

| Ep | Level | Title | Code |
|:--:|:-----:|-------|:----:|
| 01 | `BASIC` | The Generative Dilemma: GANs, VAEs, Autoregressive Models vs Diffusion | [`ep01-generative-dilemma-gans-vaes-diffusion`](ep01-generative-dilemma-gans-vaes-diffusion/) |
| 02 | `BASIC` | Mathematical Foundations: Gaussian Distributions, Markov Chains & Brownian Motion | [`ep02-mathematical-foundations-markov-gaussian-brownian`](ep02-mathematical-foundations-markov-gaussian-brownian/) |
| 03 | `BASIC` | The Forward Diffusion Process: Variance Schedules & Closed-Form Noise Sampling | [`ep03-forward-diffusion-variance-schedules-sampling`](ep03-forward-diffusion-variance-schedules-sampling/) |
| 04 | `BASIC` | The Reverse Process: Approximating Intractable Priors via Bayes' Rule & the ELBO | [`ep04-reverse-process-bayes-rule-elbo-derivation`](ep04-reverse-process-bayes-rule-elbo-derivation/) |
| 05 | `BASIC` | DDPM from Scratch (Part 1): Reparameterization Trick & Simplified Loss Function | [`ep05-ddpm-scratch-epsilon-prediction-loss`](ep05-ddpm-scratch-epsilon-prediction-loss/) |
| 06 | `BASIC` | DDPM from Scratch (Part 2): 2D Sinusoidal Positional Embeddings & Timestep Conditioning | [`ep06-ddpm-scratch-sinusoidal-embeddings-timestep-conditioning`](ep06-ddpm-scratch-sinusoidal-embeddings-timestep-conditioning/) |
| 07 | `BASIC` | U-Net Architecture Deep Dive: Residual Blocks, GroupNorm, SiLU & Skip Connections | [`ep07-unet-architecture-residual-blocks-groupnorm-silu`](ep07-unet-architecture-residual-blocks-groupnorm-silu/) |
| 08 | `BASIC` | Multi-Head Spatial Self-Attention in U-Net: QKV Projections & Receptive Fields | [`ep08-multihead-spatial-self-attention-unet`](ep08-multihead-spatial-self-attention-unet/) |
| 09 | `BASIC` | Complete DDPM Training Loop: GPU Acceleration, Gradient Accumulation & PyTorch AMP | [`ep09-complete-ddpm-training-loop-gpu-acceleration`](ep09-complete-ddpm-training-loop-gpu-acceleration/) |
| 10 | `BASIC` | DDPM Ancestral Sampling Algorithm: Reverse SDE Discretization & First Image Generation | [`ep10-ddpm-ancestral-sampling-algorithm`](ep10-ddpm-ancestral-sampling-algorithm/) |
| 11 | `BASIC` | DDIM (Denoising Diffusion Implicit Models): Non-Markovian Acceleration (1000 -> 50 Steps) | [`ep11-ddim-deterministic-sampling-acceleration`](ep11-ddim-deterministic-sampling-acceleration/) |
| 12 | `BASIC` | Continuous-Time Score-Based Modeling: Langevin Dynamics & Score Matching | [`ep12-continuous-time-score-based-modeling-langevin`](ep12-continuous-time-score-based-modeling-langevin/) |
| 13 | `BASIC` | SDEs & ODEs in Generative Modeling: Variance Preserving vs Exploding & Probability Flow | [`ep13-sdes-odes-probability-flow-song-formulation`](ep13-sdes-odes-probability-flow-song-formulation/) |
| 14 | `BASIC` | Classifier Guidance: Steering Diffusion with External Pretrained Classifiers | [`ep14-classifier-guidance-score-gradients`](ep14-classifier-guidance-score-gradients/) |
| 15 | `BASIC` | Classifier-Free Guidance (CFG): Joint Training, Dropout Conditioning & Contrast Amplification | [`ep15-classifier-free-guidance-cfg-dropout-amplification`](ep15-classifier-free-guidance-cfg-dropout-amplification/) |
| 16 | `INTERMEDIATE` | The Pixel-Space Computational Wall: Why 512x512 Diffusion Fails & The Latent Paradigm | [`ep16-pixel-space-bottleneck-latent-diffusion-paradigm`](ep16-pixel-space-bottleneck-latent-diffusion-paradigm/) |
| 17 | `INTERMEDIATE` | Variational Autoencoders (VAE) for Latents: LPIPS Loss, KL Penalty & Scaling Factors | [`ep17-variational-autoencoders-vae-lpips-latent-scaling`](ep17-variational-autoencoders-vae-lpips-latent-scaling/) |
| 18 | `INTERMEDIATE` | Stable Diffusion Architecture Deconstructed: Cross-Attention on CLIP Text Embeddings | [`ep18-stable-diffusion-cross-attention-conditioning-clip`](ep18-stable-diffusion-cross-attention-conditioning-clip/) |
| 19 | `INTERMEDIATE` | Text Conditioning Pipeline: Tokenization, CLIP Encoders, Pooled Vectors & Negative Prompts | [`ep19-text-conditioning-pipeline-clip-negative-prompts`](ep19-text-conditioning-pipeline-clip-negative-prompts/) |
| 20 | `INTERMEDIATE` | Advanced Fast Samplers: Runge-Kutta, Heun 2nd Order, DPM-Solver++ & Karras Schedules | [`ep20-advanced-fast-samplers-heun-dpm-solver-karras`](ep20-advanced-fast-samplers-heun-dpm-solver-karras/) |
| 21 | `INTERMEDIATE` | Rectified Flow & Linear Interpolation: Straight Paths Between Noise and Data | [`ep21-rectified-flow-linear-interpolation-straight-paths`](ep21-rectified-flow-linear-interpolation-straight-paths/) |
| 22 | `INTERMEDIATE` | Flow Matching vs Diffusion: Vector Field Regression, OT-CFM & Velocity Loss | [`ep22-flow-matching-vector-fields-ot-cfm-velocity-loss`](ep22-flow-matching-vector-fields-ot-cfm-velocity-loss/) |
| 23 | `INTERMEDIATE` | Diffusion Transformers (DiT): Replacing U-Net with ViT — Patchification & Scaling Laws | [`ep23-diffusion-transformers-dit-patchification-backbone`](ep23-diffusion-transformers-dit-patchification-backbone/) |
| 24 | `INTERMEDIATE` | Adaptive Layer Normalization (adaLN-Zero): Conditioning DiT on Timesteps & Classes | [`ep24-adaln-zero-conditioning-diffusion-transformers`](ep24-adaln-zero-conditioning-diffusion-transformers/) |
| 25 | `INTERMEDIATE` | Rotary Position Embeddings (RoPE) in 2D & 3D: Multi-Resolution Latent Spatial Encoding | [`ep25-rope-rotary-position-embeddings-multiresolution-diffusion`](ep25-rope-rotary-position-embeddings-multiresolution-diffusion/) |
| 26 | `INTERMEDIATE` | Stable Diffusion 3 & Flux.1 Architecture: Multimodal Diffusion Transformers (MMDiT) | [`ep26-sd3-flux-mmdit-multimodal-diffusion-transformers`](ep26-sd3-flux-mmdit-multimodal-diffusion-transformers/) |
| 27 | `INTERMEDIATE` | Text Encoders at Scale: T5-XXL, Gemma 2 & Handling Complex Descriptive Prompts | [`ep27-text-encoders-scale-t5xxl-gemma2-long-prompts`](ep27-text-encoders-scale-t5xxl-gemma2-long-prompts/) |
| 28 | `INTERMEDIATE` | Image-to-Image & Inpainting: Masked Latent Blending & Noise Injection at Timestep t | [`ep28-image-to-image-inpainting-latent-blending`](ep28-image-to-image-inpainting-latent-blending/) |
| 29 | `INTERMEDIATE` | ControlNet Architecture: Zero-Convolution Cloned Encoders & Spatial Conditioning | [`ep29-controlnet-zero-convolutions-spatial-conditioning`](ep29-controlnet-zero-convolutions-spatial-conditioning/) |
| 30 | `INTERMEDIATE` | IP-Adapter & Decoupled Cross-Attention: Image Prompts & Style Transfer Without Retraining | [`ep30-ip-adapter-decoupled-cross-attention-image-prompts`](ep30-ip-adapter-decoupled-cross-attention-image-prompts/) |
| 31 | `INTERMEDIATE` | LoRA (Low-Rank Adaptation) for Diffusion: Rank Decomposition & Weight Merging | [`ep31-lora-low-rank-adaptation-diffusion-fine-tuning`](ep31-lora-low-rank-adaptation-diffusion-fine-tuning/) |
| 32 | `INTERMEDIATE` | DoRA (Weight-Decomposed Low-Rank Adaptation): Magnitude vs Direction Decomposition | [`ep32-dora-weight-decomposed-low-rank-adaptation`](ep32-dora-weight-decomposed-low-rank-adaptation/) |
| 33 | `INTERMEDIATE` | DreamBooth & Textual Inversion: Personalizing Latent Diffusion with Prior Preservation | [`ep33-dreambooth-textual-inversion-subject-personalization`](ep33-dreambooth-textual-inversion-subject-personalization/) |
| 34 | `INTERMEDIATE` | Latent Consistency Models (LCM) & Consistency Distillation: Real-Time 2–4 Step Synthesis | [`ep34-latent-consistency-models-lcm-distillation-few-steps`](ep34-latent-consistency-models-lcm-distillation-few-steps/) |
| 35 | `INTERMEDIATE` | Adversarial Diffusion Distillation (ADD / SDXL-Turbo): 1-Step Real-Time Inference | [`ep35-adversarial-diffusion-distillation-add-sdxl-turbo-1step`](ep35-adversarial-diffusion-distillation-add-sdxl-turbo-1step/) |
| 36 | `ADVANCED` | Spatiotemporal Video Diffusion: Expanding 2D Latents to 3D Volumes & Temporal Attention | [`ep36-spatiotemporal-video-diffusion-3d-latents-temporal-attention`](ep36-spatiotemporal-video-diffusion-3d-latents-temporal-attention/) |
| 37 | `ADVANCED` | 3D Variational Autoencoders (3D Causal VAE): Temporal Compression & Video Decoding | [`ep37-3d-causal-vae-temporal-compression-zero-latency`](ep37-3d-causal-vae-temporal-compression-zero-latency/) |
| 38 | `ADVANCED` | Video DiT Foundations (Sora-Style Architecture): 3D Spatiotemporal Patches & RoPE-3D | [`ep38-video-dit-sora-architecture-3d-patches`](ep38-video-dit-sora-architecture-3d-patches/) |
| 39 | `ADVANCED` | Modern Open-Source Video Models: Architecture Deep Dive into HunyuanVideo & Wan 2.1 | [`ep39-modern-open-source-video-models-hunyuan-wan21`](ep39-modern-open-source-video-models-hunyuan-wan21/) |
| 40 | `ADVANCED` | CogVideoX & Expert Transformer Modules: Dynamic Sequence Lengths & Motion Continuity | [`ep40-cogvideox-expert-transformer-modules-motion`](ep40-cogvideox-expert-transformer-modules-motion/) |
| 41 | `ADVANCED` | Camera & Motion Control in Video Diffusion: Trajectory Conditioning & Plücker Coordinates | [`ep41-camera-motion-control-trajectory-plucker-animatediff`](ep41-camera-motion-control-trajectory-plucker-animatediff/) |
| 42 | `ADVANCED` | Continuous-Time Video Flow Matching: Velocity Fields & Variable Frame Rates | [`ep42-continuous-time-video-flow-matching-variable-fps`](ep42-continuous-time-video-flow-matching-variable-fps/) |
| 43 | `ADVANCED` | Diffusion for Audio & Music Generation: Mel-Spectrogram Latents, AudioLDM & Flow Audio | [`ep43-diffusion-audio-music-generation-spectrogram-audioldm`](ep43-diffusion-audio-music-generation-spectrogram-audioldm/) |
| 44 | `ADVANCED` | 3D Object & Scene Generation: Gaussian Splatting Diffusion & Score Distillation Sampling | [`ep44-3d-object-scene-generation-gaussian-splatting-sds`](ep44-3d-object-scene-generation-gaussian-splatting-sds/) |
| 45 | `ADVANCED` | RLHF for Diffusion: Direct Preference Optimization (Diffusion-DPO) & Score Reweighting | [`ep45-rlhf-diffusion-dpo-direct-preference-optimization`](ep45-rlhf-diffusion-dpo-direct-preference-optimization/) |
| 46 | `ADVANCED` | Quantization of Giant Diffusion Transformers: FP8 (E4M3/E5M2), INT4 Weight-Only & AWQ | [`ep46-quantization-giant-dit-fp8-int4-awq`](ep46-quantization-giant-dit-fp8-int4-awq/) |
| 47 | `ADVANCED` | Memory Optimization: FlashAttention-3, Chunked Cross-Attention & DeepSpeed ZeRO | [`ep47-memory-optimization-flashattention3-chunked-cross-attention`](ep47-memory-optimization-flashattention3-chunked-cross-attention/) |
| 48 | `ADVANCED` | High-Throughput Production Serving: TensorRT, Torch Compile & CUDA Graph Capture | [`ep48-high-throughput-production-serving-tensorrt-torch-compile`](ep48-high-throughput-production-serving-tensorrt-torch-compile/) |
| 49 | `ADVANCED` | Real-Time Interactive Streaming Diffusion: Sub-50ms Latency Pipelines & WebRTC | [`ep49-realtime-interactive-streaming-diffusion-sub50ms-webrtc`](ep49-realtime-interactive-streaming-diffusion-sub50ms-webrtc/) |
| 50 | `ADVANCED` | Production Capstone (Part 1): Training an End-to-End Rectified Flow Transformer | [`ep50-production-capstone-rectified-flow-transformer-scratch`](ep50-production-capstone-rectified-flow-transformer-scratch/) |
| 51 | `ADVANCED` | Production Capstone (Part 2): Distilling the Flow Transformer into a 2-Step Generator | [`ep51-production-capstone-distilling-flow-transformer-2step`](ep51-production-capstone-distilling-flow-transformer-2step/) |
| 52 | `ADVANCED` | Production Capstone (Part 3): Scalable Multi-GPU Triton & FastAPI Cluster with Prometheus | [`ep52-production-capstone-multigpu-triton-fastapi-cluster`](ep52-production-capstone-multigpu-triton-fastapi-cluster/) |

---

## 🚀 Getting Started & Environment Setup

```bash
# Clone the repository
git clone https://github.com/lets-learn-with-ajay/codecraft-masterclass.git
cd codecraft-masterclass/07-diffusion-models/ep01-generative-dilemma-gans-vaes-diffusion

# Recommended environment (PyTorch 2.4+ with CUDA / MPS)
pip install torch torchvision torchaudio diffusers transformers accelerate
python model.py
```

---

## ⭐ Support

If this series helped you master modern generative deep learning, please **star ⭐ this repository** and **subscribe** to [@letslearnwithajay](https://youtube.com/@letslearnwithajay)!
