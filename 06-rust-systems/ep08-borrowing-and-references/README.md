# Episode 08: Borrowing & References: Shared (&T) vs Mutable (&mut T)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: BASIC](https://img.shields.io/badge/Level-BASIC-emerald?style=for-the-badge)](#)

## 📌 Summary
Accessing data without taking ownership. Shared immutable references (&T), exclusive mutable references (&mut T), and the fundamental Aliasing XOR Mutability rule that prevents data races.

## 🎯 Key Takeaways
- References let you view or mutate data without transferring ownership, avoiding unnecessary cloning
- Aliasing XOR Mutability: You can have any number of &T references OR exactly one &mut T, never both at once
- The borrow checker guarantees references are always non-null and valid, preventing dangling pointers

## 🔍 Topics & Keywords
- `Rust borrowing tutorial`
- `Rust mutable references`
- `Aliasing XOR Mutability Rust`
- `Rust borrow checker explained`

## 🚀 How to Run

```bash
cargo check
cargo run
```
