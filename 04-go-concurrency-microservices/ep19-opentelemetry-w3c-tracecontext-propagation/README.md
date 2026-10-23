# Episode 19: Distributed Tracing with OpenTelemetry & W3C TraceContext Propagation across HTTP & gRPC

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
End-to-end request visibility. Injecting and extracting W3C TraceContext headers across HTTP, gRPC, and Kafka messages in Go, creating child spans, and exporting to Jaeger.

## 🎯 Key Takeaways
- Inject traceparent headers into outgoing HTTP and gRPC metadata to preserve distributed request context
- Instrument gRPC client and server interceptors to capture latency spans automatically
- Export structured trace spans to Jaeger and Datadog for visual distributed bottleneck diagnosis

## 🔍 Topics & Keywords
- `OpenTelemetry Go distributed tracing`
- `W3C TraceContext Go`
- `gRPC OpenTelemetry interceptor`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
