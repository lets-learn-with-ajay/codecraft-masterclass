# Episode 41: Data Parallelism with Rayon: Work-Stealing Pools & Parallel Iterators

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Converting single-core algorithms to multi-core in one line. The Rayon library, parallel iterators (par_iter()), divide-and-conquer parallelism (rayon::join), and the work-stealing runtime.

## 🎯 Key Takeaways
- Rayon converts sequential iterators to parallel work-stealing pipelines simply by replacing iter() with par_iter()
- Work-stealing schedulers automatically balance compute loads across threads when task execution times vary
- Rayon guarantees data race freedom at compile time using Rust's Send and Sync invariants

## 🔍 Topics & Keywords
- `Rust Rayon tutorial`
- `Rayon par_iter`
- `work stealing scheduler rayon`
- `Rust data parallelism`

## 🚀 How to Run

```bash
cargo check
cargo run
```
