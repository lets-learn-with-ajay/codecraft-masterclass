# Episode 52: Foreign Function Interface (FFI): Interoperating with C/C++ Libraries Safely

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Bridging language ecosystems. Calling C libraries from Rust using extern "C", automatic header parsing with bindgen, exporting Rust functions to C with cbindgen, and memory ownership across boundaries.

## 🎯 Key Takeaways
- extern "C" defines the standard C calling convention for cross-language binary interoperability
- bindgen automatically generates safe Rust type definitions and function signatures from C header files
- Memory allocated by C (malloc) must be freed by C (free); memory allocated by Rust must be freed by Rust

## 🔍 Topics & Keywords
- `Rust C FFI tutorial`
- `bindgen rust tutorial`
- `cbindgen export rust to C`
- `extern C rust calling conventions`

## 🚀 How to Run

```bash
cargo check
cargo run
```
