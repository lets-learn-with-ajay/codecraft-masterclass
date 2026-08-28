# Episode 05: Distributed Rate Limiting: Token Bucket vs Sliding Window Log

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Protecting systems from DDoS and abusive traffic with Redis Lua scripts and token bucket / sliding-window algorithms.

## 🎯 Key Takeaways
- Local in-memory rate limiting fails in multi-server load-balanced clusters without centralized state synchronization.
- Atomic Redis Lua scripts prevent race conditions and network round-trips during token replenishments and decrements.
- Sliding window logs offer ultra-high precision, while token buckets offer memory-efficient, high-throughput enforcement.

## 🔍 Topics Covered
- `distributed rate limiter system design`
- `token bucket redis Lua script`

## 🚀 How to Run

```bash
python simulation.py
```
