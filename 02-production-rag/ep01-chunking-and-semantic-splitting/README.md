# Episode 01: The Chunking Dilemma: Semantic Splitting & Hierarchical Retrieval

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Production RAG](https://img.shields.io/badge/Track-02_Production_RAG-818cf8?style=for-the-badge)](../README.md)

## 📌 Summary
Why naive fixed-size chunking destroys context. Implementing semantic splitting and parent-document retrieval.

## 🎯 Key Takeaways
- Fixed chunking splits critical sentences across arbitrary token boundaries.
- Semantic splitting measures embedding similarity deltas between consecutive sentences.
- Parent document retrievers match on small, precise chunks but return the broader parent context to the LLM.

## 🔍 Topics Covered
- `advanced RAG semantic chunking`
- `parent document retriever python`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
