# Episode 22: Context Window Packing & Lost-in-the-Middle Mitigation with Attention Sorting

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Maximizing LLM reasoning fidelity. Overcoming the 'lost-in-the-middle' phenomenon by sorting retrieved chunks based on relevance scores, placing critical facts at prompt extremes.

## 🎯 Key Takeaways
- LLMs exhibit U-shaped attention curves, paying highest attention to tokens at the beginning and end of prompts
- Chunks placed in the middle of long contexts are 30% more likely to be ignored during generation
- Attention sorting alternates placing highest-scoring chunks at the top and bottom of the context block

## 🔍 Topics & Keywords
- `lost in the middle LLM RAG`
- `context window packing`
- `attention sorting RAG prompt`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
