# Episode 02: Robust Worker Pools & Fan-Out/Fan-In Pipeline Patterns

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Go Concurrency & Microservices](https://img.shields.io/badge/Track-04_Go_Microservices-00ADD8?style=for-the-badge)](../README.md)

## 📌 Summary
Building production concurrent pipelines with buffered channels, worker pools, and context cancellation.

## 🎯 Key Takeaways
- Worker pools strictly bound concurrent resource consumption (memory, sockets, database handles).
- Fan-out distributes independent tasks across CPU cores; fan-in multiplexes results back into a single pipeline channel.
- Always pass `context.Context` to cleanly propagate cancellation signals and deadlines across goroutine trees.

## 🔍 Topics Covered
- `Go worker pool pattern tutorial`
- `fan out fan in Go concurrency`

## 🚀 How to Run

```bash
go run main.go
```
