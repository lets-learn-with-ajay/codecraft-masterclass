# Episode 29: Fine-Grained Guardrails & Content Moderation with Llama Guard & Edge Middleware

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLHembivxlGE4)
[![Track: Modern Full-Stack AI with Next.js 15 & Vercel AI SDK](https://img.shields.io/badge/Track-03_nextjs15_fullstack_ai-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Hardening public AI endpoints. Screening user inputs and LLM completions against safety policies using Llama Guard, regex pattern matchers, and edge middleware before token streaming begins.

## 🎯 Key Takeaways
- Edge middleware screens incoming user prompts before invoking expensive frontier models
- Llama Guard classifies prompts across safety hazard taxonomies (hate, violence, self-harm, jailbreaks)
- Blocks malicious inputs at the edge with custom user-friendly rejection messages

## 🔍 Topics & Keywords
- `Llama Guard Next.js middleware`
- `AI safety content moderation`
- `edge prompt filtering Next.js 15`

## 🚀 How to Run

```bash
npm install
npm run dev
```
