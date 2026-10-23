# Episode 30: Cargo Mastery: Multi-Crate Workspaces, Feature Flags & Dependencies

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Scaling codebases to enterprise grade. Structuring Cargo workspaces with shared dependencies, feature flags for conditional compilation, dependency overriding with path/patch, and cargo vendor.

## 🎯 Key Takeaways
- Cargo workspaces allow cohesive crates to share a single target/ build cache and unified Cargo.lock
- Feature flags enable zero-overhead conditional compilation for optional functionality and lightweight builds
- Workspace inheritance (workspace = true) centralizes version management across dozens of sub-crates

## 🔍 Topics & Keywords
- `Cargo workspaces tutorial`
- `Rust feature flags default`
- `Rust enterprise multi crate`
- `Cargo.toml workspace dependencies`

## 🚀 How to Run

```bash
cargo check
cargo run
```
