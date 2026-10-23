# Episode 23: Kernel-Level Observability: eBPF Microservice Tracing with Go and Cilium/ebpf

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Zero-overhead production telemetry. Writing eBPF programs in C, loading and managing them from pure Go with Cilium/ebpf, and inspecting network sockets and system calls without modifying application code.

## 🎯 Key Takeaways
- eBPF runs sandboxed verification programs inside the Linux kernel to monitor socket and system call activity
- The Cilium/ebpf library loads compiled eBPF bytecode and reads kernel ring buffers directly in pure Go
- Captures inbound/outbound HTTP/gRPC traffic with zero modification to existing microservice codebases

## 🔍 Topics & Keywords
- `cilium ebpf Go tutorial`
- `eBPF microservice tracing Go`
- `Linux kernel observability Go`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
