# Episode 20: Metadata Filtering at Scale: HNSW Payload Indexing & Multi-Tenant Partitioning in Qdrant

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Instant filtered vector searches. Configuring payload indexes in Qdrant, combining pre-filtering with HNSW vector traversal, and implementing multi-tenant data isolation.

## 🎯 Key Takeaways
- Post-filtering vector search results leads to low recall when filters match few documents
- Payload indexing in Qdrant integrates boolean filters directly into the HNSW graph traversal
- Enforces strict multi-tenant tenant_id isolation without sacrificing search speed or recall

## 🔍 Topics & Keywords
- `Qdrant payload indexing`
- `metadata filtering vector search`
- `multi tenant vector database`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
