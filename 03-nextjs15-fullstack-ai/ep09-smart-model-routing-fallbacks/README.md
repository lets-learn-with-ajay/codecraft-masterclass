# Episode 09: Smart Model Routing & Multi-Provider Fallbacks

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Next.js 15 Full-Stack AI](https://img.shields.io/badge/Track-03_Next.js_15_AI-2dd4bf?style=for-the-badge)](../README.md)

## 📌 Summary
Dynamically routing queries to cheap small models (Claude Haiku / GPT-4o-mini) vs frontier models, with automated provider failover.

## 🎯 Key Takeaways
- Route simple classifications and entity extraction to sub-cent fast models and complex coding/reasoning to frontier models.
- Automatic fallback triggers when a primary provider experiences downtime or rate limits (503 / 429).
- Reduces monthly LLM inference costs by up to 60% without sacrificing end-user quality.

## 🔍 Topics Covered
- `smart model routing LLM Next.js`
- `multi provider LLM fallback Vercel AI SDK`

## 🚀 How to Run

```bash
npm install
npm run dev
```
