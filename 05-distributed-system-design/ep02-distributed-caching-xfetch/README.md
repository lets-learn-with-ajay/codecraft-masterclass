# Episode 02: Distributed Caching & Cache Stampede Defense with Redis

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Designing multi-tier caching architectures with write-through vs cache-aside patterns and probabilistic early expiration (XFetch).

## 🎯 Key Takeaways
- Cache stampedes crash downstream databases when popular hot keys expire simultaneously under heavy traffic.
- Probabilistic early recomputation (XFetch algorithm) asynchronously refreshes keys before formal expiration.
- Redis Cluster partitioning provides horizontal cache scaling with 16,384 deterministic hash slots.

## 🔍 Topics Covered
- `cache stampede redis system design`
- `XFetch probabilistic early expiration`

## 🚀 How to Run

```bash
python simulation.py
```
