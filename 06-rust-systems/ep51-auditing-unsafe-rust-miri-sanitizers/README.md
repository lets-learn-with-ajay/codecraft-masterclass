# Episode 51: Auditing Unsafe Rust with Miri & LLVM Sanitizers (ASan, TSan)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Verifying unsafe correctness. Running Miri (Mid-level IR interpreter) to catch pointer aliasing violations, Stacked Borrows rules, use-after-free, and integrating AddressSanitizer (ASan) into CI.

## 🎯 Key Takeaways
- Miri executes Rust code in an interpreted environment, checking memory access against the Stacked Borrows model
- Miri detects undefined behavior, unaligned pointer dereferences, and memory leaks that tests miss
- Run cargo miri test in continuous integration pipelines for any crate that uses unsafe blocks

## 🔍 Topics & Keywords
- `cargo miri tutorial`
- `Rust stacked borrows miri`
- `AddressSanitizer rust ASan`
- `auditing unsafe rust`

## 🚀 How to Run

```bash
cargo check
cargo run
```
