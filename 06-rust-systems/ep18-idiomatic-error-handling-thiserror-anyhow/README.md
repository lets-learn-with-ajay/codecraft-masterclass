# Episode 18: Idiomatic Error Handling: The ? Operator, Custom Enums, thiserror & anyhow

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Writing production error handling without boilerplate. Error propagation with the question mark (?) operator, From trait conversions, thiserror for libraries, and anyhow for applications.

## 🎯 Key Takeaways
- The ? operator provides ergonomic early returns, automatically converting error types via the From trait
- Use thiserror to create strongly-typed, enum-based error hierarchies for reusable libraries
- Use anyhow::Result and Context for application-level code to attach rich diagnostic context to errors

## 🔍 Topics & Keywords
- `Rust error handling ? operator`
- `thiserror vs anyhow`
- `Rust custom error enum`
- `Rust error propagation`

## 🚀 How to Run

```bash
cargo check
cargo run
```
