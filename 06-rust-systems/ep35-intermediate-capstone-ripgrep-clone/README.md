# Episode 35: Intermediate Capstone Project: Building a Blazing-Fast File Search Tool (Mini-ripgrep)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLJUkDq7ZYhII)
[![Track: Modern Rust Systems & Architecture Masterclass](https://img.shields.io/badge/Track-06_rust_systems-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Bringing Part 2 together: A multi-threaded, regex-powered recursive file search utility using clap for CLI parsing, rayon for parallel directory traversal, regex matching, and colored output.

## 🎯 Key Takeaways
- Combine clap, regex, and filesystem traversal into a unified, high-performance command line tool
- Gracefully handle file permission errors and non-UTF-8 binary files without crashing
- Proper project modularization allows independent unit testing of matchers, printers, and walkers

## 🔍 Topics & Keywords
- `Rust ripgrep clone project`
- `Rust parallel file search`
- `Rust intermediate capstone`
- `Rust project tutorial`

## 🚀 How to Run

```bash
cargo check
cargo run
```
