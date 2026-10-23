# Episode 29: Project Organization: Modules, Crates, Paths & Visibility Rules

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Architecting multi-file Rust projects. Declaring modules with mod, importing items with use, file hierarchy conventions (mod.rs vs foo.rs), visibility scopes (pub, pub(crate), pub(super)), and re-exports.

## 🎯 Key Takeaways
- Modules control encapsulation and privacy: all items in Rust are private by default to their parent module
- pub(crate) restricts visibility to the current crate, preventing internal implementation details from leaking
- Use pub use (re-exporting) to present a clean, intuitive public API while keeping internal file layout modular

## 🔍 Topics & Keywords
- `Rust modules tutorial`
- `Rust pub crate visibility`
- `Rust project structure multi file`
- `Rust mod use re exports`

## 🚀 How to Run

```bash
cargo check
cargo run
```
