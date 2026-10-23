# Episode 25: Distributed Rate Limiting: Sliding Window Counter with Redis & Atomic Local Leaky Buckets

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Two-tier rate limiting architecture. Combining sub-millisecond in-memory atomic leaky buckets with Redis sliding window counters using atomic Lua scripts to handle 100,000+ requests/sec.

## 🎯 Key Takeaways
- Pure Redis rate limiters create central network latency bottlenecks on high-traffic microservices
- Two-tier architectures evaluate local in-memory leaky buckets first, syncing batch tokens to Redis asynchronously
- Atomic Lua scripts execute sliding window checks and token increments within a single Redis round trip

## 🔍 Topics & Keywords
- `distributed rate limiter Go Redis`
- `sliding window counter Lua script`
- `two tier rate limiting microservice`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
