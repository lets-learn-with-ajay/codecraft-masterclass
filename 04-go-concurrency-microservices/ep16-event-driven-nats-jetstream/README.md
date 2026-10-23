# Episode 16: Event-Driven Microservices with NATS JetStream & Go: Ultra-Low Latency Pub/Sub

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Sub-millisecond event streaming. Building resilient publisher and consumer microservices with NATS JetStream in Go, subject hierarchy routing, consumer groups, and deduplication windows.

## 🎯 Key Takeaways
- NATS JetStream delivers sub-millisecond publish/subscribe latency with minimal memory footprint
- Durable consumers track message acknowledgments and automatically redeliver unacknowledged tasks
- Subject-based routing enables fine-grained event filtering without dedicated broker queue creation

## 🔍 Topics & Keywords
- `NATS JetStream Go tutorial`
- `event driven microservices Golang`
- `ultra low latency pub sub Go`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
