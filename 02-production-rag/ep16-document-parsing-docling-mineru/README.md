# Episode 16: Document Parsing at Scale: Parsing Complex Tables, Equations & Multi-Column Layouts

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
High-fidelity document ingestion. Parsing scientific papers and financial balance sheets using Docling and MinerU, converting complex tables to clean markdown, and preserving mathematical formulas.

## 🎯 Key Takeaways
- Standard PyPDF text extraction scrambles multi-column layouts and destroys financial tables
- Docling uses vision models to reconstruct document reading order and table bounding boxes
- Structured markdown output preserves row and column relationships for accurate LLM reasoning

## 🔍 Topics & Keywords
- `Docling PDF parser python`
- `MinerU document extraction`
- `financial table parsing RAG`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
