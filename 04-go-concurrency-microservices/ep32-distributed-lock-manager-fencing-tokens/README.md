# Episode 32: Building a Distributed Lock Manager with Fencing Tokens in Go

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Preventing silent data corruption. Why naive distributed locks fail during GC pauses, implementing monotonically increasing fencing tokens, and validating token order at the storage layer.

## 🎯 Key Takeaways
- A client holding a lock may experience a stop-the-world GC pause, allowing its lock lease to expire unnoticed
- Fencing tokens assign an incrementing integer ID to each lock acquisition
- The backend storage engine rejects any write carrying a fencing token lower than the highest seen token

## 🔍 Topics & Keywords
- `fencing tokens distributed lock Go`
- `Martin Kleppmann distributed lock`
- `safe distributed locking Golang`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
