# Episode 07: Ownership & Move Semantics: The Golden Rule of Memory Safety

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: BASIC](https://img.shields.io/badge/Level-BASIC-emerald?style=for-the-badge)](#)

## 📌 Summary
The core foundation of Rust. The three ownership rules, shallow copies vs moves, why assignment transfers ownership, Copy types vs Clone types, and deterministic destruction with the Drop trait.

## 🎯 Key Takeaways
- Each value in Rust has exactly one owner at any given moment; when the owner leaves scope, it is dropped
- Assigning heap-allocated types transfers ownership (move), invalidating the previous variable to prevent double frees
- Types implementing Copy duplicate bitwise on the stack without heap allocation overhead

## 🔍 Topics & Keywords
- `Rust ownership tutorial beginner`
- `Rust move semantics explained`
- `Rust Copy vs Clone trait`
- `Rust Drop trait RAII`

## 🚀 How to Run

```bash
cargo check
cargo run
```
