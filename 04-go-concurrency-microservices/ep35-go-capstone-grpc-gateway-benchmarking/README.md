# Episode 35: Go Microservices Capstone (Part 3): Distributed Key-Value Engine — gRPC Gateway & Benchmarking

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Series Capstone Grand Finale: Exposing high-throughput gRPC and REST APIs, instrumenting OpenTelemetry tracing, and benchmarking the cluster under 100,000 requests/sec with zero packet drops.

## 🎯 Key Takeaways
- Expose gRPC and HTTP/JSON endpoints with protobuf schema validation and graceful connection pooling
- Instrument OpenTelemetry spans and Prometheus metrics tracking latency percentiles across cluster nodes
- Achieves sustained 100,000 requests/second throughput with p99 latency under 4 milliseconds

## 🔍 Topics & Keywords
- `distributed KV store finale Go`
- `gRPC gateway microservice Go`
- `benchmark distributed system Go`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
