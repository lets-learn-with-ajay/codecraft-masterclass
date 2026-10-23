# Episode 11: Vision-Language RAG with ColPali: Multi-Vector Page Patch Embeddings & MaxSim Scoring

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Bypassing brittle OCR pipelines. Rendering document pages directly as images, generating multi-vector patch representations with ColPali vision-language models, and executing late-interaction MaxSim retrieval.

## 🎯 Key Takeaways
- Eliminates OCR parsing errors on complex multi-column layouts, technical diagrams, and tables
- ColPali generates patch-level vector embeddings that capture visual and semantic context simultaneously
- MaxSim scoring computes late-interaction similarity across all query tokens and document visual patches

## 🔍 Topics & Keywords
- `ColPali RAG tutorial`
- `vision language document retrieval`
- `MaxSim multi vector search`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
