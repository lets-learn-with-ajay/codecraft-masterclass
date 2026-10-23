# Episode 26: High-Performance Zero-Copy I/O: Kernel sendfile, splice, and io_uring in Go

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Saturating 10Gbps network interfaces. Eliminating userspace buffer copies using Linux sendfile and splice system calls, and asynchronous kernel event submission with io_uring in Go.

## 🎯 Key Takeaways
- Traditional read/write cycles copy data 4 times between disk, kernel page cache, and userspace memory
- sendfile transfers bytes directly between kernel page cache and network sockets with zero CPU copies
- io_uring submits batched, asynchronous I/O requests to the kernel without invoking blocking syscalls

## 🔍 Topics & Keywords
- `zero copy IO Go sendfile`
- `Linux splice Golang`
- `io_uring Go high performance IO`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
