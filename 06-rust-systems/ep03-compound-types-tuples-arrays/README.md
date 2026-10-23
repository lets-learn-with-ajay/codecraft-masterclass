# Episode 03: Compound Data Types: Fixed-Size Stack Arrays & Multi-Type Tuples

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: BASIC](https://img.shields.io/badge/Level-BASIC-emerald?style=for-the-badge)](#)

## 📌 Summary
Grouping values in Rust. Tuples for heterogeneous fixed-length values, tuple indexing, destructuring patterns, and stack-allocated fixed-size arrays [T; N] with compile-time bounds checking.

## 🎯 Key Takeaways
- Tuples combine heterogeneous values into a single compound type accessible via dot notation or destructuring
- Arrays in Rust have fixed length known at compile time and allocate contiguously on the stack
- Attempting to access an array out of bounds panics deterministically rather than returning garbage memory

## 🔍 Topics & Keywords
- `Rust tuples destructuring`
- `Rust stack arrays [T; N]`
- `Rust array bounds checking`
- `Rust compound types`

## 🚀 How to Run

```bash
cargo check
cargo run
```
