# Episode 10: Scaling Vector DBs: HNSW Parameter Tuning & Product Quantization

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Production RAG](https://img.shields.io/badge/Track-02_Production_RAG-818cf8?style=for-the-badge)](../README.md)

## 📌 Summary
Optimizing vector databases for million-scale production workloads with HNSW indexing, scalar quantization, and sub-10ms latency.

## 🎯 Key Takeaways
- Tune `M` and `efConstruction` parameters for the optimal recall vs build-time/RAM trade-off.
- Scalar and Product Quantization reduces embedding RAM footprint by up to 75% while retaining 98%+ recall.
- Filtered vector search indexing patterns enable scalable multi-tenant isolation.

## 🔍 Topics Covered
- `vector database HNSW tuning`
- `product quantization embeddings latency`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
