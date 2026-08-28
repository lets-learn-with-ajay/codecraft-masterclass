# 🌐 Track 3: Modern Full-Stack AI with Next.js 15 & Vercel AI SDK

> **Build production-ready, streaming AI web applications with Generative UI**

[![YouTube Playlist](https://img.shields.io/badge/YouTube-Playlist-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/playlist?list=PLHembivxlGE4)
[![Domain: Full-Stack Web](https://img.shields.io/badge/Domain-Full--Stack_Web-2dd4bf?style=for-the-badge)](#)

---

## 📖 Overview

In this track, you will build modern, end-to-end full-stack AI web applications using **Next.js 15 (App Router)**, **React Server Components**, and the **Vercel AI SDK**. Master real-time token streaming, Generative UI widgets, Zod structured outputs, Supabase pgvector semantic search, Drizzle ORM persistence, Upstash rate limiting, Inngest background queues, and edge deployment.

---

## 🗺️ Episodes & Roadmap

| Ep | Episode Title | Key Highlights | Code |
|:--:|---------------|----------------|:----:|
| **01** | [Next.js 15 App Router & Token Streaming with Vercel AI SDK Core](ep01-streaming-app-router/) | App Router Route Handlers, `streamText`, Server-Sent Events, `useChat` | [📂 Code](ep01-streaming-app-router/) |
| **02** | [Generative UI: Streaming Dynamic React Components from LLM Output](ep02-generative-ui-components/) | Streaming interactive React widgets (weather, charts) directly from tool calls | [📂 Code](ep02-generative-ui-components/) |
| **03** | [Type-Safe Structured Output with Zod & Function Calling](ep03-structured-json-zod/) | Schema validation with `generateObject` and Zod, runtime TypeScript types | [📂 Code](ep03-structured-json-zod/) |
| **04** | [In-Database Vector Search with Supabase pgvector & Server Actions](ep04-vector-search-supabase/) | Direct PostgreSQL semantic search, Server Actions, HNSW indexing | [📂 Code](ep04-vector-search-supabase/) |
| **05** | [Multi-Modal AI: Vision Understanding, Audio Transcripts & Voice UI](ep05-multimodal-ai-vision-voice/) | Image chat buffers, Whisper transcription, Web Audio API streaming | [📂 Code](ep05-multimodal-ai-vision-voice/) |
| **06** | [Persistent Chat Sessions & Database Sync with Drizzle ORM](ep06-persistent-chat-sessions-drizzle/) | Relational session storage, Drizzle ORM, optimistic UI rendering | [📂 Code](ep06-persistent-chat-sessions-drizzle/) |
| **07** | [Rate Limiting, Upstash Redis & Edge Deployment](ep07-rate-limiting-production/) | Sliding-window rate limiters, token cost protection, edge caching | [📂 Code](ep07-rate-limiting-production/) |
| **08** | [Durable Background AI Workflows with Inngest & Webhooks](ep08-background-ai-jobs-inngest/) | Serverless long-running LLM workflows, automatic retries, webhook updates | [📂 Code](ep08-background-ai-jobs-inngest/) |
| **09** | [Smart Model Routing & Multi-Provider Fallbacks](ep09-smart-model-routing-fallbacks/) | Dynamic model routing (Haiku / 4o-mini vs frontier), provider failover | [📂 Code](ep09-smart-model-routing-fallbacks/) |
| **10** | [Production Deployment, Streaming Error Boundaries & OpenTelemetry](ep10-production-edge-deployment-observability/) | Edge deployment, stream error boundaries, OpenTelemetry token tracing | [📂 Code](ep10-production-edge-deployment-observability/) |

---

## 🛠️ Tech Stack & Prerequisites

- **Frontend / Framework**: Next.js 15, React 19, TypeScript, Tailwind CSS, shadcn/ui
- **AI Tooling**: Vercel AI SDK Core & UI (`ai`, `@ai-sdk/openai`, `@ai-sdk/anthropic`)
- **Database & ORM**: PostgreSQL, Supabase (pgvector), Drizzle ORM
- **Async & Caching**: Upstash Redis, Inngest
- **Validation**: Zod

---

## ⚡ Quick Start

```bash
cd 03-nextjs15-fullstack-ai/ep01-streaming-app-router
npm install
npm run dev
```
