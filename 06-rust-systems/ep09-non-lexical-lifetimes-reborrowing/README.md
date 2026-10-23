# Episode 09: Non-Lexical Lifetimes (NLL) & Reborrowing Mechanics

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: BASIC](https://img.shields.io/badge/Level-BASIC-emerald?style=for-the-badge)](#)

## 📌 Summary
How modern Rust tracks reference scopes with precision. Non-Lexical Lifetimes (NLL), how borrow scopes end at last point of use rather than closing braces, and safe reborrowing patterns.

## 🎯 Key Takeaways
- Non-Lexical Lifetimes (NLL) end borrows as soon as the reference is last used, not at the end of the curly brace scope
- Reborrowing allows passing a shorter-lived mutable reference from an existing mutable reference without moving it
- Understanding NLL eliminates 80% of beginner borrow checker fighting

## 🔍 Topics & Keywords
- `Rust Non Lexical Lifetimes NLL`
- `Rust reborrowing patterns`
- `borrow checker scope rules`

## 🚀 How to Run

```bash
cargo check
cargo run
```
