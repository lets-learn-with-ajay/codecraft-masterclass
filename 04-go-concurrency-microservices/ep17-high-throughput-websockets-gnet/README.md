# Episode 17: High-Throughput WebSockets with Epoll: Scaling 1,000,000 Concurrent Connections with gnet

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Breaking the 1M connection barrier. Bypassing standard net/http goroutine-per-connection memory limits using event-driven, non-blocking network frameworks (gnet) and Linux epoll.

## 🎯 Key Takeaways
- Standard net/http allocates a 2–8KB goroutine per connection, consuming gigabytes of RAM at 1M connections
- gnet uses Linux epoll / macOS kqueue event loops to multiplex thousands of sockets on single OS threads
- Enables high-density WebSocket servers capable of serving millions of concurrent idle connections

## 🔍 Topics & Keywords
- `gnet Golang tutorial`
- `epoll WebSockets Go`
- `C1000K problem Go concurrency`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
