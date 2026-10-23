# Episode 34: RAG Capstone (Part 2): Enterprise Document Brain — Hybrid Neo4j GraphRAG & Self-Correcting Router

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Series Capstone: Combining graphs and vectors. Ingesting corporate knowledge graphs into Neo4j, implementing an agentic query router, and dynamic web search fallback with CRAG.

## 🎯 Key Takeaways
- Integrates Neo4j entity-relation graphs with Qdrant vector search into a unified retrieval orchestrator
- The router analyzes query intent to dynamically determine whether to execute vector, graph, or SQL search
- Corrective RAG verification grades retrieved context quality and falls back to live web search when necessary

## 🔍 Topics & Keywords
- `GraphRAG Neo4j capstone`
- `hybrid vector graph search`
- `self correcting RAG router`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
