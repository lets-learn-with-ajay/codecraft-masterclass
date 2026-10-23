# Episode 43: Async Internals: Building a Custom Future, Poll & Wakers from Scratch

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Under the hood of async execution. Manually implementing the Future trait with fn poll(self: Pin<&mut Self>, cx: &mut Context), understanding Poll::Ready vs Poll::Pending, and how Wakers notify the event loop.

## 🎯 Key Takeaways
- The Future trait requires a poll method returning Poll::Ready(T) or Poll::Pending
- When returning Poll::Pending, the future must store the Context's Waker to wake the runtime when data arrives
- Spurious wakeups are normal: executors re-poll futures when awakened by external hardware or timers

## 🔍 Topics & Keywords
- `Rust manual Future implementation`
- `Rust Waker explained`
- `Rust async under the hood`
- `Poll Ready Pending`

## 🚀 How to Run

```bash
cargo check
cargo run
```
