# Episode 26: Iterators: Functional Pipelines with Zero Performance Cost

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
The crown jewel of idiomatic Rust: Iterators. The Iterator trait and next(), into_iter() vs iter() vs iter_mut(), adapter chaining (map, filter, fold, zip, enumerate), and why iterators beat C for-loops.

## 🎯 Key Takeaways
- Rust iterators are lazy: no computation occurs until a consumer like collect() or sum() is invoked
- into_iter consumes collections; iter borrows immutably; iter_mut borrows mutably
- The compiler unrolls and vectorizes iterator chains into machine instructions that match or beat hand-written C

## 🔍 Topics & Keywords
- `Rust iterators tutorial`
- `Rust into_iter vs iter`
- `Rust iterator adapters map filter`
- `Rust zero cost iterators`

## 🚀 How to Run

```bash
cargo check
cargo run
```
