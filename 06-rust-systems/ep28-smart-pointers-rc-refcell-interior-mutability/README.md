# Episode 28: Smart Pointers (Part 2): Shared Ownership with Rc<T> & RefCell<T>

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Navigating complex graph structures in single-threaded programs. Reference counting with Rc<T>, clone costs, interior mutability with RefCell<T>, and deferring borrow checking to runtime.

## 🎯 Key Takeaways
- Rc<T> enables multiple owners of the same heap allocation in single-threaded contexts via reference counting
- RefCell<T> enforces Rust's borrowing rules at runtime rather than compile time via borrow() and borrow_mut()
- Combining Rc<RefCell<T>> allows multiple owners to share and mutate data (e.g. graph nodes, UI trees)

## 🔍 Topics & Keywords
- `Rust Rc smart pointer`
- `Rust RefCell interior mutability`
- `Rust Rc RefCell graph`
- `borrow checker runtime RefCell`

## 🚀 How to Run

```bash
cargo check
cargo run
```
