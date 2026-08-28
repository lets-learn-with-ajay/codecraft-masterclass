# Episode 03: Cross-Encoder Re-Ranking & Context Compression

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Production RAG](https://img.shields.io/badge/Track-02_Production_RAG-818cf8?style=for-the-badge)](../README.md)

## 📌 Summary
Boosting retrieval accuracy by re-ranking top-30 candidate documents into top-3 high-density context chunks.

## 🎯 Key Takeaways
- Bi-encoders are fast for initial large-scale candidate retrieval; cross-encoders are deeply accurate for pairwise scoring.
- Re-ranking eliminates noisy and irrelevant chunks before they reach the LLM context window.
- Drastically reduces token consumption and eliminates the lost-in-the-middle / needle-in-haystack phenomenon.

## 🔍 Topics Covered
- `cross encoder reranking RAG`
- `Cohere rerank python BGE reranker`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
