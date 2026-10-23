# Episode 62: Kernel-Level Networking with eBPF in Rust (The Aya Framework)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Running sandboxed bytecode inside the Linux kernel. Packet filtering with XDP, kernel maps, writing safe userspace-to-kernel programs in pure Rust using Aya, and sub-microsecond firewalling.

## 🎯 Key Takeaways
- eBPF allows executing sandboxed Rust bytecode directly inside the Linux kernel without kernel module risks
- Aya enables writing both the kernel-space eBPF program and userspace loader in 100% pure Rust
- XDP (eXpress Data Path) intercepts and filters network packets directly at the NIC driver before OS stack traversal

## 🔍 Topics & Keywords
- `Rust eBPF Aya tutorial`
- `XDP packet filtering rust`
- `Linux kernel programming rust`
- `Aya framework eBPF`

## 🚀 How to Run

```bash
cargo check
cargo run
```
