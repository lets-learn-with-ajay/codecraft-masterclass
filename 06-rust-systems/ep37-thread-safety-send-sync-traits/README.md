# Episode 37: Thread Safety Guarantees: The Send & Sync Marker Traits Demystified

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Why Rust prevents data races at compile time. The Send trait (transferring ownership across threads), the Sync trait (sharing references across threads), and auto-trait propagation rules.

## 🎯 Key Takeaways
- Send indicates ownership of the type can be transferred across thread boundaries safely
- Sync indicates references to the type (&T) can be shared across multiple threads concurrently
- Types are automatically Send and Sync if all their constituent fields are Send and Sync (e.g. Rc is !Send)

## 🔍 Topics & Keywords
- `Rust Send and Sync traits`
- `Rust thread safety compile time`
- `what makes a type Send`
- `Rust auto traits`

## 🚀 How to Run

```bash
cargo check
cargo run
```
