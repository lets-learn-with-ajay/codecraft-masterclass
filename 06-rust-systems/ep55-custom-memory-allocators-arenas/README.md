# Episode 55: Custom Memory Allocators & Arenas: Jemalloc, Bump Allocators & Cache Locality

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Bypassing global allocator lock contention. The GlobalAlloc trait, configuring jemalloc and mimalloc in Rust, implementing a high-speed bump arena allocator, and optimizing for 64-byte CPU cache lines.

## 🎯 Key Takeaways
- The GlobalAlloc trait allows replacing the system allocator with high-throughput allocators like Jemalloc
- Bump allocators deallocate hundreds of temporary objects simultaneously in O(1) time with a pointer reset
- Aligning data structures to 64-byte CPU cache lines prevents false sharing across concurrent CPU cores

## 🔍 Topics & Keywords
- `Rust GlobalAlloc custom allocator`
- `Rust jemalloc configuration`
- `bump arena allocator rust`
- `cache line false sharing rust`

## 🚀 How to Run

```bash
cargo check
cargo run
```
