# Episode 08: Corrective RAG (CRAG) & Self-RAG: Dynamic Web Search Fallback

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Production RAG](https://img.shields.io/badge/Track-02_Production_RAG-818cf8?style=for-the-badge)](../README.md)

## 📌 Summary
Building self-evaluating RAG pipelines that grade retrieved context and automatically trigger live web search when documents are insufficient.

## 🎯 Key Takeaways
- Retrieval grading nodes classify context quality into Relevant, Ambiguous, or Irrelevant categories.
- Ambiguous or Irrelevant retrieval triggers search APIs (Tavily, DuckDuckGo) for real-time web augmentation.
- Guarantees accurate answers and minimizes hallucinations even when the internal vector database lacks coverage.

## 🔍 Topics Covered
- `Corrective RAG CRAG tutorial`
- `Self RAG dynamic web fallback python`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
