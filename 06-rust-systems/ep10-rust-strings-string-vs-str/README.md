# Episode 10: The Mystery of Rust Strings: String vs &str Explained Simply

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: BASIC](https://img.shields.io/badge/Level-BASIC-emerald?style=for-the-badge)](#)

## 📌 Summary
Solving the number-one stumbling block for Rust newcomers: understanding owned, heap-allocated, growable String versus borrowed string slices (&str), UTF-8 encoding, and indexing rules.

## 🎯 Key Takeaways
- &str is an immutable UTF-8 slice view (pointer + length) into memory anywhere (binary, stack, or heap)
- String is an owned, growable UTF-8 buffer (pointer + length + capacity) allocated on the heap
- Rust prohibits direct integer indexing string[i] because UTF-8 characters have variable byte lengths

## 🔍 Topics & Keywords
- `Rust String vs &str explained`
- `how Rust strings work`
- `Rust string slices tutorial`
- `Rust UTF-8 string indexing`

## 🚀 How to Run

```bash
cargo check
cargo run
```
