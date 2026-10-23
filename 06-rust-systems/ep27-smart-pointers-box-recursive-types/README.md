# Episode 27: Smart Pointers (Part 1): Box<T> & Recursive Data Structures

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Allocating on the heap with purpose. Understanding Box<T>, why recursive types require indirection to have a known compile-time size, building a Linked List and Binary Search Tree.

## 🎯 Key Takeaways
- Box<T> allocates values on the heap and owns the allocation, deallocating automatically via Drop on scope exit
- Recursive types (e.g. trees, linked lists) require Box<T> to provide a fixed pointer size at compile time
- Deref coercion allows Box<T> to be passed directly to functions expecting &T without manual dereferencing

## 🔍 Topics & Keywords
- `Rust Box smart pointer`
- `Rust recursive data structures Box`
- `Rust binary search tree`
- `Rust heap allocation Box`

## 🚀 How to Run

```bash
cargo check
cargo run
```
