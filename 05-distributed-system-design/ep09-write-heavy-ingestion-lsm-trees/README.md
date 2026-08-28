# Episode 09: High-Throughput Ingestion: LSM Trees, ClickHouse & Time-Series DBs

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Architecting write-heavy telemetry and clickstream ingestion pipelines capable of handling 1,000,000 events/second using Log-Structured Merge (LSM) trees.

## 🎯 Key Takeaways
- B-trees degrade significantly under heavy random writes; LSM trees convert random writes into ultra-fast sequential append operations.
- In-memory MemTables flush to immutable SSTables on disk, organized with background merge-compaction passes.
- Columnar analytical storage engines (ClickHouse) provide up to 100x faster aggregations compared to row-based engines.

## 🔍 Topics Covered
- `LSM tree write heavy architecture`
- `ClickHouse high throughput ingestion system design`

## 🚀 How to Run

```bash
python simulation.py
```
