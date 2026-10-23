# Episode 15: Stateful Agent Tool Caching & Dynamic Tool Catalog Discovery via MCP

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Eliminating tool definition overhead in high-frequency graphs. Caching MCP tool catalogs across graph invocations, dynamic tool filtering based on user intent, and reducing LLM context consumption.

## 🎯 Key Takeaways
- Re-fetching MCP tool catalogs on every graph invocation introduces unnecessary latency
- In-memory catalog caching with TTL invalidation keeps tool definitions synchronized efficiently
- Intent-based tool filtering selects only the top-K relevant tools to prevent prompt bloat

## 🔍 Topics & Keywords
- `MCP tool caching LangGraph`
- `dynamic tool catalog discovery`
- `reduce agent tool token cost`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
