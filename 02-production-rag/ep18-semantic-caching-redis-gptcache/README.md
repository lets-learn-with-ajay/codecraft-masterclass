# Episode 18: Semantic Caching with Redis & GPTCache: Eliminating 80% of Redundant LLM Invocations

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Slashing production inference latency. Setting up vector-based semantic response caching with Redis and GPTCache, configuring cosine similarity thresholds, and cache invalidation strategies.

## 🎯 Key Takeaways
- Exact keyword caching misses rephrased user queries asking the identical question
- Semantic caching embeds incoming queries and returns cached responses above similarity thresholds
- Cuts 80% of redundant API costs and drops response latency from 3,000ms to sub-15ms

## 🔍 Topics & Keywords
- `semantic cache Redis`
- `GPTCache tutorial python`
- `reduce LLM API cost cache`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
