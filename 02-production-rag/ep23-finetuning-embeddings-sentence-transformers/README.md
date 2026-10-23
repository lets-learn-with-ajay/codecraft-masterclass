# Episode 23: Fine-Tuning Domain Embedding Models with Sentence Transformers & MNRL

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Adapting embeddings to specialized domains (medical, legal, financial). Fine-tuning bi-encoders using MultipleNegativesRankingLoss, hard negative mining, and evaluating on custom benchmark splits.

## 🎯 Key Takeaways
- Off-the-shelf embedding models struggle with domain-specific jargon, acronyms, and product IDs
- MultipleNegativesRankingLoss optimizes vector space separation using positive and mined hard negative pairs
- Achieves 15–25% accuracy gains on specialized proprietary enterprise documentation

## 🔍 Topics & Keywords
- `fine tune embedding model python`
- `MultipleNegativesRankingLoss tutorial`
- `sentence transformers domain adaptation`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
