# Episode 39: Message Passing Concurrency: std::sync::mpsc & Crossbeam Channels

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Do not communicate by sharing memory; share memory by communicating. Multi-producer, single-consumer channels (mpsc), bounded vs unbounded buffers, backpressure, and crossbeam channels.

## 🎯 Key Takeaways
- mpsc channels allow multiple producer threads to send messages to a single consumer worker thread
- Always prefer bounded channels (sync_channel) to establish backpressure and prevent unbounded memory growth
- crossbeam-channel provides high-performance multi-producer multi-consumer (MPMC) channel topologies

## 🔍 Topics & Keywords
- `Rust mpsc channels`
- `crossbeam channel rust`
- `Rust bounded channels backpressure`
- `actor pattern rust`

## 🚀 How to Run

```bash
cargo check
cargo run
```
