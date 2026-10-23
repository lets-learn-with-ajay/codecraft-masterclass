# Episode 46: Tokio Channels & Async Primitives: mpsc, broadcast, watch, oneshot & Notify

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Coordinating async tasks. Bounded mpsc for worker pipelines with backpressure, broadcast for 1-to-many event streaming, watch for config state distribution, oneshot for request-response, and Notify.

## 🎯 Key Takeaways
- Always use bounded channels (tokio::sync::mpsc::channel) so senders wait when buffers are full (backpressure)
- broadcast multiplexes messages to dozens of receivers; lagging receivers receive a RecvError::Lagged error
- watch channels hold a single value and notify subscribers only when the value changes, ideal for live configs

## 🔍 Topics & Keywords
- `Tokio channels mpsc broadcast`
- `Tokio watch channel`
- `Tokio oneshot pattern`
- `async backpressure tokio`

## 🚀 How to Run

```bash
cargo check
cargo run
```
