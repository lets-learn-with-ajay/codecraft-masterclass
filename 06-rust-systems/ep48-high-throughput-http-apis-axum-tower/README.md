# Episode 48: High-Throughput HTTP APIs with Axum: Extractors, State & Tower Middleware

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Building production web services. Type-safe routing in Axum, request body extractors (Json, Path, Query), injecting shared state via Arc<AppState>, and composable Tower middleware (rate limiting, tracing).

## 🎯 Key Takeaways
- Axum leverages Rust's type system to validate request paths, headers, and JSON payloads at compile time
- Shared application state is injected safely via Extension or State(Arc<AppState>) with zero lock overhead
- Tower middleware allows composable request/response pipelines for authentication, metrics, and rate limiting

## 🔍 Topics & Keywords
- `Axum tutorial Rust 2026`
- `Axum state extractors`
- `Tower middleware Rust`
- `high performance REST API rust`

## 🚀 How to Run

```bash
cargo check
cargo run
```
