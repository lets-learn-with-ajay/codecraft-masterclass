# Episode 24: Fine-Tuning Cross-Encoder Re-Rankers for High-Precision Enterprise Domains

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Maximizing re-ranking precision. Training cross-encoder scoring models on domain-specific query-document pairs, contrastive loss functions, and deploying on Triton Inference Server.

## 🎯 Key Takeaways
- Cross-encoders process query and candidate text jointly, modeling deep token-to-token interactions
- Fine-tuning on domain data ensures nuanced relevance distinctions that general models miss
- Deploying on Triton Inference Server provides batched GPU acceleration for sub-20ms re-ranking

## 🔍 Topics & Keywords
- `fine tune cross encoder`
- `custom reranker training python`
- `Triton inference server reranker`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
