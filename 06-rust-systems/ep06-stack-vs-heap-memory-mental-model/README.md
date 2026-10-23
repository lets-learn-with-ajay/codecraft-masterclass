# Episode 06: The Rust Mental Model: Stack vs Heap Demystified

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: BASIC](https://img.shields.io/badge/Level-BASIC-emerald?style=for-the-badge)](#)

## 📌 Summary
Demystifying how program memory actually works from first principles. Stack frames, fast pointer bumping, dynamic heap allocations via OS allocators, and why Rust needs no garbage collector.

## 🎯 Key Takeaways
- Stack memory stores fixed-size data with instantaneous push/pop LIFO pointer movement (sub-nanosecond)
- Heap memory stores dynamically sized data via OS memory allocator pointers, incurring metadata and lookup overhead
- Rust tracks pointer lifetimes at compile time, eliminating both GC pause spikes and manual memory leaks

## 🔍 Topics & Keywords
- `Rust stack vs heap explained`
- `how memory works in Rust`
- `Rust without garbage collector`
- `stack pointer LIFO`

## 🚀 How to Run

```bash
cargo check
cargo run
```
