# Episode 32: Edge Compute & Distributed State: Deploying Compute to Cloudflare Workers with Global Replicas

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
The serverless edge frontier. Deploying serverless logic to Cloudflare Workers / Fly.io, connecting to read-replicas near users, and managing write propagation back to primary regions.

## 🎯 Key Takeaways
- Edge compute runs serverless V8 isolates in hundreds of data centers worldwide within 10ms of users
- Route read queries to localized database replicas and forward mutations securely to the primary region
- Enables instant global page rendering with dynamic personalization and zero cold-start penalties

## 🔍 Topics & Keywords
- `Cloudflare Workers edge compute`
- `distributed state edge serverless`
- `Fly io global read replicas`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
