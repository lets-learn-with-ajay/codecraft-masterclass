# Episode 44: The Mystery of Pinning: Pin<P>, Self-Referential Structs & !Unpin Invariants

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Solving the hardest concept in async Rust. Why self-referential structs break when moved in memory, how Pin<P> guarantees an object will never move again, Unpin vs !Unpin, and pin-project.

## 🎯 Key Takeaways
- Self-referential structs hold internal pointers to their own fields; moving them in memory invalidates those pointers
- Pin<P> wraps a pointer to guarantee that the underlying pointee will never be moved or deallocated prematurely
- Types implementing Unpin can be safely unpinned; async state machines are !Unpin to protect internal pointers

## 🔍 Topics & Keywords
- `Rust Pin explained`
- `Rust self referential structs`
- `Pin Unpin !Unpin`
- `why does async Rust need Pin`

## 🚀 How to Run

```bash
cargo check
cargo run
```
