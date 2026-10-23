# Episode 13: Matryoshka Representation Learning (MRL): Elastic Dimensionality & Memory Compression

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Slashing vector database memory footprint by 75%. Truncating high-dimensional embeddings (1536 to 256 dimensions) using Matryoshka models with negligible retrieval loss and sub-millisecond search speed.

## 🎯 Key Takeaways
- Matryoshka embeddings pack the most critical semantic information into the first N dimensions
- Enables two-stage retrieval: fast filtering on 256 dimensions followed by re-scoring top-100 on 1536
- Reduces vector database RAM consumption and indexing costs by up to 75%

## 🔍 Topics & Keywords
- `Matryoshka embeddings RAG`
- `MRL vector compression`
- `reduce vector database RAM cost`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
