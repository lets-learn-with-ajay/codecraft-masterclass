# Episode 16: Standard Collections (Part 1): Dynamic Vectors (Vec), Slices & Preallocation

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Deep dive into Rust's most common collection: Vec<T>. Memory layout (pointer, length, capacity), amortized reallocation growth factor, Vec::with_capacity, and slicing (&[T]).

## 🎯 Key Takeaways
- Vec<T> stores data contiguously on the heap with a 3-word pointer, length, and capacity header on the stack
- Preallocating capacity with Vec::with_capacity eliminates expensive heap reallocations and copies
- Passing &[T] instead of &Vec<T> maximizes flexibility, accepting both vectors and fixed arrays

## 🔍 Topics & Keywords
- `Rust Vec tutorial`
- `Rust with_capacity performance`
- `Rust vector memory layout`
- `Rust slices &[T]`

## 🚀 How to Run

```bash
cargo check
cargo run
```
