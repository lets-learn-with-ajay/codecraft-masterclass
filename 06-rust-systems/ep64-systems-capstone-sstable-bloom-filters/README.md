# Episode 64: Systems Capstone (Part 2): SSTables, Sparse Indexing & Bloom Filters

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Flushing memory to disk. Implementing Sorted String Tables (SSTables), sparse in-memory index tables for binary search, false-positive-resistant Bloom Filters, and background compaction threads.

## 🎯 Key Takeaways
- SSTables store immutable, sorted key-value pairs on disk, eliminating expensive random write seeks
- Bloom filters prevent unnecessary disk seeks for keys that do not exist within an SSTable file
- Background compaction merges multiple small SSTable runs into single consolidated files, pruning tombstones

## 🔍 Topics & Keywords
- `SSTable implementation rust`
- `bloom filter rust tutorial`
- `sparse index binary search rust`
- `LSM compaction engine`

## 🚀 How to Run

```bash
cargo check
cargo run
```
