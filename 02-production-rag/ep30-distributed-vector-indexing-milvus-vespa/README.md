# Episode 30: Distributed Vector Indexing: Sharding Billion-Scale Vector Collections with Milvus & Vespa

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Architecting billion-scale search engines. Cluster topology design, segment compaction, query coordinator routing, and high availability across distributed vector database nodes.

## 🎯 Key Takeaways
- Single-node vector databases hit physical memory ceilings at ~50 million vectors
- Distributed query coordinators broadcast searches across shards and merge top-K candidates
- Separate write nodes and query nodes to maintain sub-20ms search latencies during heavy ingestion

## 🔍 Topics & Keywords
- `Milvus billion scale vector search`
- `Vespa distributed indexing`
- `shard vector database cluster`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
