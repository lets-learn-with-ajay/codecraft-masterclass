# Episode 12: Late Chunking & Jina Embeddings: Context-Preserving Token Span Pooling

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Solving the chunk boundary dilemma. Passing 8,192-token document contexts through long-context embedding models first, then applying mean pooling across specific chunk spans to preserve holistic context.

## 🎯 Key Takeaways
- Traditional chunking severs pronouns, coreferences, and global definitions across boundaries
- Late chunking computes contextual representations for every token before span pooling
- Significantly boosts retrieval precision on ambiguous sentences without increasing token storage

## 🔍 Topics & Keywords
- `Late Chunking RAG tutorial`
- `Jina embeddings late chunking`
- `context preserving chunk pooling`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
