# Episode 17: Standard Collections (Part 2): HashMap, HashSet, BTreeMap & The Entry API

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Key-value data structures in Rust. Hash collision defenses with SipHash, BTreeMap for sorted key iteration, and atomic inspect-and-modify workflows using the powerful Entry API.

## 🎯 Key Takeaways
- Rust HashMap defaults to SipHash 1-3 to defend against HashDoS denial-of-service attacks
- The Entry API (entry(key).or_insert()) eliminates double-lookups by inspecting and inserting atomically
- BTreeMap maintains sorted key ordering and predictable memory boundaries for range queries

## 🔍 Topics & Keywords
- `Rust HashMap tutorial`
- `Rust Entry API or_insert`
- `Rust BTreeMap vs HashMap`
- `Rust HashSet`

## 🚀 How to Run

```bash
cargo check
cargo run
```
