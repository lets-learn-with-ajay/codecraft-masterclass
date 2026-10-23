# Episode 17: Change Data Capture (CDC): Streaming Database Mutations with Debezium & Kafka Connect

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Real-time data synchronization. Reading PostgreSQL WAL and MySQL binlogs directly with Debezium, streaming change events through Kafka Connect, and building resilient search index update pipelines.

## 🎯 Key Takeaways
- Dual-writing to databases and message queues introduces silent inconsistency during network failures
- CDC reads transaction logs directly from the storage engine, capturing every committed change with zero data loss
- Kafka Connect automatically manages connector tasks, schema evolutions, and offset tracking

## 🔍 Topics & Keywords
- `Change Data Capture CDC Debezium`
- `Kafka Connect database streaming`
- `Postgres WAL replication Debezium`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
