# Episode 21: Distributed Unique ID Generation: Snowflake IDs, ULIDs, and UUIDv7 for High-Throughput DBs

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Generating 64-bit k-sortable unique IDs at scale. Twitter Snowflake architecture (timestamp + worker ID + sequence), ULIDs, and why UUIDv7 prevents B-tree fragmentation in PostgreSQL.

## 🎯 Key Takeaways
- Standard random UUIDv4 causes severe B-tree page fragmentation and random disk I/O thrashing in databases
- k-sortable IDs (Snowflake, UUIDv7) encode Unix millisecond timestamps in leading bits for sequential insertions
- Snowflake IDs generate 64-bit compact integers locally across thousands of worker nodes without central locks

## 🔍 Topics & Keywords
- `Twitter Snowflake ID tutorial`
- `UUIDv7 vs UUIDv4 database index`
- `k-sortable unique ID distributed system`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
