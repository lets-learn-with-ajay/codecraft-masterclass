# Episode 30: High-Frequency Distributed Counters: Aggregation & Batch Flushing with Redis & Kafka

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Handling 10,000,000 events/second. Why relational atomic increments lock tables, designing distributed counter trees, probabilistic counting with HyperLogLog, and micro-batch flushes.

## 🎯 Key Takeaways
- Row-level database locks on single counter rows create catastrophic serialization bottlenecks
- Shard counters across N independent keys or aggregate counts in local memory buffers before flushing batches
- HyperLogLog estimates unique counts (cardinality) with 99% accuracy using only 12KB of fixed memory

## 🔍 Topics & Keywords
- `distributed counter system design`
- `HyperLogLog tutorial Redis`
- `high throughput counting Kafka`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
