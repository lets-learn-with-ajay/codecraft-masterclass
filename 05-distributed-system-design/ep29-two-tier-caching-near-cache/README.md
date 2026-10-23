# Episode 29: Distributed Caching Topologies: Two-Tier L1/L2 Caches, Near-Caches & Consistency Invalidation

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Sub-microsecond data retrieval. Architecting two-tier caching: in-memory L1 near-caches inside application pods paired with centralized L2 Redis clusters, with pub/sub bus invalidation broadcasts.

## 🎯 Key Takeaways
- Querying Redis over the network incurs 1–2ms of TCP round-trip latency per request
- L1 near-caches store hot keys in local application process memory for sub-microsecond retrieval
- Redis Pub/Sub or Kafka invalidation channels broadcast eviction signals to all app nodes upon key updates

## 🔍 Topics & Keywords
- `two tier caching architecture`
- `near cache distributed systems`
- `Redis L1 L2 cache invalidation`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
