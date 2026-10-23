# Episode 36: Multi-Threaded Concurrency: std::thread, JoinHandles & Moving State

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
True multi-core parallelism. Spawning OS threads with std::thread::spawn, transferring ownership into threads with move closures, joining threads via JoinHandle, and handling panics safely.

## 🎯 Key Takeaways
- std::thread::spawn launches true native OS threads scheduled by the kernel across multi-core CPUs
- move closures transfer ownership of required variables into the thread, satisfying the 'static lifetime bound
- JoinHandle::join blocks until the worker thread terminates, returning a Result that catches worker panics

## 🔍 Topics & Keywords
- `Rust multi threading tutorial`
- `std thread spawn move`
- `Rust JoinHandle`
- `Rust thread panic recovery`

## 🚀 How to Run

```bash
cargo check
cargo run
```
