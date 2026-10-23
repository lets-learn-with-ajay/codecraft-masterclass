# Episode 60: Systems Profiling & Microbenchmarking: cargo-flamegraph & Criterion.rs

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Pinpointing performance bottlenecks scientifically. Statistical microbenchmarking with Criterion.rs, detecting regressions, CPU sampling with cargo-flamegraph, and cache miss analysis.

## 🎯 Key Takeaways
- Criterion detects micro-optimizations and performance regressions with rigorous statistical confidence intervals
- Flamegraphs visualize CPU sampling profiles to instantly highlight algorithmic hotspots in production code
- Always inspect disassembly with cargo-asm to verify compiler inlining and loop vectorization

## 🔍 Topics & Keywords
- `Criterion rs benchmark tutorial`
- `cargo flamegraph profiling`
- `Rust CPU profiling`
- `cache miss optimization rust`

## 🚀 How to Run

```bash
cargo check
cargo run
```
