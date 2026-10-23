# Episode 31: Token Budget Optimization: Semantic Caching & Small-Model Speculative Routing

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Slashing enterprise LLM costs by 70%. Semantic prompt caching with Qdrant/Redis, speculative routing using fast sub-cent SLMs (Claude 3.5 Haiku / GPT-4o-mini), and token quota enforcement.

## 🎯 Key Takeaways
- Semantic caching checks vector similarity on incoming queries before invoking frontier models
- Route 80% of routine classification and formatting tasks to cheap small language models
- Enforce token quotas and hard spending caps at the checkpointer level to prevent runaway billing

## 🔍 Topics & Keywords
- `semantic cache AI agent`
- `speculative model routing`
- `reduce LangGraph API costs`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
