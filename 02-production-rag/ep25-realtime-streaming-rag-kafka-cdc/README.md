# Episode 25: Real-Time Streaming RAG: Ingesting Kafka CDC Streams into Vector Indexes

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Zero-latency knowledge freshness. Building an event-driven indexing pipeline consuming Change Data Capture (CDC) events from Kafka/Debezium, real-time chunking, and sub-second vector updates.

## 🎯 Key Takeaways
- Batch nightly re-indexing leaves retrieval systems operating on stale, outdated context
- Kafka CDC pipelines stream row updates immediately upon database commit
- Micro-batch embedding workers update vector indexes within 500ms of document creation

## 🔍 Topics & Keywords
- `streaming RAG Kafka CDC`
- `real time vector indexing`
- `Debezium vector database sync`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
