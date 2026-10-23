# Episode 14: gRPC Bidirectional Streaming: Building a Real-Time High-Throughput Telemetry Service

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Real-time microservice communication. Implementing full-duplex bidirectional gRPC streams, handling HTTP/2 flow control windows, client keep-alives, and graceful disconnection recovery.

## 🎯 Key Takeaways
- Bidirectional gRPC streaming enables simultaneous full-duplex message exchange over a single TCP stream
- Implement client-side backpressure monitoring to prevent overflowing HTTP/2 flow control buffers
- Configure keep-alive client parameters to detect dead TCP connections across cloud load balancers

## 🔍 Topics & Keywords
- `gRPC bidirectional streaming Golang`
- `real time telemetry Go gRPC`
- `HTTP/2 flow control gRPC Go`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
