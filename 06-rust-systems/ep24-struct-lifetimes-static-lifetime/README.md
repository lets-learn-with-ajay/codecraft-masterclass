# Episode 24: Struct Lifetimes, Multiple Lifetimes & The 'static Lifetime

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Holding references inside structs. Struct lifetime syntax struct Buffer<'a>, tying struct lifetimes to borrowed data, multiple distinct lifetime parameters, and what 'static really means.

## 🎯 Key Takeaways
- A struct holding a reference (&'a T) can never outlive the data it references, guaranteed by the compiler
- The 'static lifetime denotes data that can live for the entire duration of the program (e.g. string literals)
- T: 'static means the type owns its data or only holds 'static references, a critical bound for thread spawning

## 🔍 Topics & Keywords
- `Rust struct lifetimes`
- `Rust static lifetime`
- `Rust multiple lifetimes`
- `Rust holding references in structs`

## 🚀 How to Run

```bash
cargo check
cargo run
```
