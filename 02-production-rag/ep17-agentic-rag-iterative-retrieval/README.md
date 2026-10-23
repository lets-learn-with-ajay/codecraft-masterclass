# Episode 17: Agentic RAG: Iterative Retrieval, Query Routing & Self-Reflective Planning

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Moving from static to active retrieval. Designing agentic RAG loops that evaluate retrieval adequacy, rewrite missing search queries, and route between vector stores, SQL databases, and search engines.

## 🎯 Key Takeaways
- Static single-hop retrieval fails when user questions require information from multiple sources
- Evaluation nodes assess retrieved context sufficiency before determining whether to search again
- Dynamic routers dispatch queries to the optimal specialized data store (vector, graph, or relational)

## 🔍 Topics & Keywords
- `Agentic RAG LangGraph`
- `iterative retrieval LLM`
- `self reflective RAG pipeline`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
