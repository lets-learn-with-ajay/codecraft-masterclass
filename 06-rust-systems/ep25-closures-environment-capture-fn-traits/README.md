# Episode 25: Closures: Anonymous Functions, Environment Capture & The Fn Traits

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Mastering Rust closures. Syntax, type inference, capturing by reference (&T), by mutable reference (&mut T), or by move (move keyword), and the three closure traits: Fn, FnMut, and FnOnce.

## 🎯 Key Takeaways
- Rust closures automatically infer the most permissive way to capture variables from their surrounding scope
- FnOnce consumes captured variables by value; FnMut mutates captured variables; Fn borrows immutably
- Use move closures when passing closures across thread boundaries to transfer ownership of captured state

## 🔍 Topics & Keywords
- `Rust closures tutorial`
- `Rust Fn FnMut FnOnce`
- `Rust move closures`
- `Rust closure environment capture`

## 🚀 How to Run

```bash
cargo check
cargo run
```
