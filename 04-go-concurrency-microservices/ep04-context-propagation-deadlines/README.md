# Episode 04: Context Propagation, Cascading Timeouts & Graceful Deadlines

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Go Concurrency & Microservices](https://img.shields.io/badge/Track-04_Go_Microservices-00ADD8?style=for-the-badge)](../README.md)

## 📌 Summary
Mastering Go's `context.Context` to propagate deadlines, trace metadata, and cascade cancellations across distributed systems.

## 🎯 Key Takeaways
- Context propagation prevents orphaned goroutines from continuously burning CPU and leaking database connections.
- Cascading timeouts automatically abort downstream RPC calls and database queries when request deadlines expire.
- Context values should strictly carry request-scoped metadata (auth tokens, correlation IDs, trace spans).

## 🔍 Topics Covered
- `Golang context propagation tutorial`
- `Go context with timeout graceful cancel`

## 🚀 How to Run

```bash
go run main.go
```
