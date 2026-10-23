# Episode 59: Production Observability: Structured Tracing, OpenTelemetry & Jaeger

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Observability in mission-critical deployments. Structured spans across async tasks with tracing-subscriber, distributed tracing with OpenTelemetry, and exporting spans to Jaeger and Datadog.

## 🎯 Key Takeaways
- The tracing ecosystem tracks spans across async task yield points where traditional logging loses context
- Spans record execution duration, enter/exit events, and structured metadata for every incoming request
- OpenTelemetry exporters ship distributed traces to Jaeger and Datadog for end-to-end latency analysis

## 🔍 Topics & Keywords
- `Rust tracing subscriber tutorial`
- `Rust OpenTelemetry Jaeger`
- `async structured logging tracing`
- `distributed tracing rust`

## 🚀 How to Run

```bash
cargo check
cargo run
```
