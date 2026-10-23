# Episode 14: Basic Error Handling: Result, panic!, unwrap vs expect

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: BASIC](https://img.shields.io/badge/Level-BASIC-emerald?style=for-the-badge)](#)

## 📌 Summary
Differentiating recoverable errors from unrecoverable bugs. The Result<T, E> type (Ok/Err), panic! vs exit codes, and when it is acceptable to use unwrap vs expect during development.

## 🎯 Key Takeaways
- Result<T, E> models recoverable errors, forcing callers to inspect failure states explicitly
- panic! aborts or unwinds the stack for unrecoverable bugs like contract violations
- Always prefer expect("descriptive context") over unwrap() so failures explain the root cause

## 🔍 Topics & Keywords
- `Rust Result Ok Err`
- `Rust panic vs return Result`
- `Rust unwrap vs expect`
- `Rust beginner error handling`

## 🚀 How to Run

```bash
cargo check
cargo run
```
