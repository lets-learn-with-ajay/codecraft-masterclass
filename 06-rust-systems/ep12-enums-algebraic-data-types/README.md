# Episode 12: Enums & Algebraic Data Types: Expressive Tagged Unions Without Overhead

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: BASIC](https://img.shields.io/badge/Level-BASIC-emerald?style=for-the-badge)](#)

## 📌 Summary
Modeling business domains cleanly. Enums with associated data payloads, unit variants, struct variants, tuple variants, and exhaustive pattern matching with match expressions.

## 🎯 Key Takeaways
- Rust enums can embed distinct data payloads inside each variant, acting as type-safe tagged unions
- Exhaustive match expressions guarantee all edge cases are handled before compilation succeeds
- Niche optimization packs enums efficiently, often consuming zero extra bytes over raw pointers

## 🔍 Topics & Keywords
- `Rust enums algebraic data types`
- `Rust tagged unions enums`
- `Rust enum data variants`
- `Rust match pattern matching`

## 🚀 How to Run

```bash
cargo check
cargo run
```
