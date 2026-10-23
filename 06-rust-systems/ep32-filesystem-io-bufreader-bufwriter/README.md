# Episode 32: High-Performance Filesystem & Stream I/O: BufReader & BufWriter

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Working with files and streams safely. std::fs operations, streaming with Read and Write traits, eliminating syscall thrashing with BufReader and BufWriter, and robust Path/PathBuf manipulation.

## 🎯 Key Takeaways
- BufReader and BufWriter batch operations into 8KB buffers, reducing expensive kernel syscall overhead by 100x
- Path is a borrowed filesystem path slice; PathBuf is an owned, growable path buffer analogous to &str and String
- Always handle I/O errors explicitly using the ? operator, wrapping paths in contextual error messages

## 🔍 Topics & Keywords
- `Rust file IO tutorial`
- `Rust BufReader vs raw read`
- `Rust PathBuf Path`
- `Rust std io Read Write`

## 🚀 How to Run

```bash
cargo check
cargo run
```
