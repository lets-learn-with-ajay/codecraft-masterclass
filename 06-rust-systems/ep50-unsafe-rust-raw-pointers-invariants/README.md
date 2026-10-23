# Episode 50: Demystifying unsafe Rust: Raw Pointers, Undefined Behavior & Safety Contracts

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
The discipline of unsafe code. The 5 superpowers of unsafe, raw pointers (*const T, *mut T), constructing safe abstraction boundaries, documented safety invariants, and avoiding Undefined Behavior (UB).

## 🎯 Key Takeaways
- unsafe Rust disables the borrow checker for specific superpowers (raw pointers, FFI, mutable statics)
- unsafe does not turn off the type checker or borrow checker elsewhere; it declares developer responsibility
- Always wrap unsafe code in clean, audited safe functions with explicit // SAFETY comments documenting invariants

## 🔍 Topics & Keywords
- `unsafe Rust tutorial`
- `Rust raw pointers *const *mut`
- `Rust undefined behavior UB`
- `safe abstraction over unsafe`

## 🚀 How to Run

```bash
cargo check
cargo run
```
