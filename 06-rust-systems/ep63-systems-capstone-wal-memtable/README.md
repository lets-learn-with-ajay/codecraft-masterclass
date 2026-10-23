# Episode 63: Systems Capstone (Part 1): Building a Distributed Storage Engine (WAL & MemTable)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Architectural Capstone: Constructing a high-performance in-memory and on-disk storage engine. Write-Ahead Logging (WAL) for crash resilience, concurrent SkipList MemTables, and atomics.

## 🎯 Key Takeaways
- Write-Ahead Logs append mutations sequentially to disk before updating the in-memory MemTable for crash safety
- Concurrent SkipLists enable lock-free, sorted in-memory insertions with logarithmic lookup complexity
- Clean domain separation allows independent testing of memory tables and disk serialization layers

## 🔍 Topics & Keywords
- `Rust key value store from scratch`
- `LSM tree implementation rust`
- `write ahead log rust`
- `SkipList memtable rust`

## 🚀 How to Run

```bash
cargo check
cargo run
```
