# Episode 22: Static Monomorphization vs Dynamic Dispatch: impl Trait vs dyn Trait

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Under the hood of Rust polymorphism. Static dispatch (monomorphization) with impl Trait for inlined zero-cost performance vs dynamic dispatch with dyn Trait (vtables) for heterogeneous collections.

## 🎯 Key Takeaways
- Monomorphization generates specialized machine code for each concrete type at compile time with zero runtime cost
- Dynamic dispatch (Box<dyn Trait>) trades a slight vtable pointer indirection for heterogeneous runtime collections
- Object safety rules dictate whether a trait can be turned into a dynamic trait object

## 🔍 Topics & Keywords
- `Rust monomorphization explained`
- `impl Trait vs dyn Trait`
- `Rust vtables dynamic dispatch`
- `Rust object safety`

## 🚀 How to Run

```bash
cargo check
cargo run
```
