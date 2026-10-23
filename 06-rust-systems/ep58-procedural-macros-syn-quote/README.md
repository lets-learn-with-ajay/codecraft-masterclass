# Episode 58: Metaprogramming (Part 2): Procedural Derive Macros with syn & quote

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Writing compiler extensions in Rust. Custom derive macros (#[derive(MyTrait)]), parsing AST tokens with syn, generating code with quote, proc-macro crates, and attribute macros.

## 🎯 Key Takeaways
- Procedural macros are compiler plugins written in Rust that execute during compilation to transform token streams
- syn parses raw TokenStreams into structured AST syntax trees; quote generates new TokenStreams cleanly
- Custom derive macros eliminate thousands of lines of boilerplate for serialization, validation, and routing

## 🔍 Topics & Keywords
- `Rust procedural macro tutorial`
- `syn and quote rust derive`
- `Rust proc macro crate`
- `custom derive rust`

## 🚀 How to Run

```bash
cargo check
cargo run
```
