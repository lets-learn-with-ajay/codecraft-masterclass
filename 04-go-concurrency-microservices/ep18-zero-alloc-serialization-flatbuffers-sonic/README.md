# Episode 18: Zero-Allocation Serialization: Replacing JSON with FlatBuffers, Cap'n Proto & Sonic

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Eliminating CPU serialization bottlenecks. Benchmarking standard encoding/json against SIMD-accelerated JSON parsers (Sonic) and zero-copy binary serialization formats (FlatBuffers).

## 🎯 Key Takeaways
- Standard encoding/json relies heavily on runtime reflection and heap allocations
- Bytedance Sonic uses AVX2 SIMD instructions to parse JSON at hardware speeds with zero allocations
- FlatBuffers access serialized data directly from byte buffers without unpacking or copying

## 🔍 Topics & Keywords
- `zero allocation serialization Go`
- `bytedance sonic JSON Go`
- `FlatBuffers tutorial Golang`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
