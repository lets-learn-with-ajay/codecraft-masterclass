# Episode 29: CPU Profiling & Microbenchmarking: Finding Allocation Hotspots with pprof & Flamegraphs

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Scientific performance tuning. Profiling live production Go services with net/http/pprof, capturing CPU, heap, and block profiles, and identifying algorithmic bottlenecks with flamegraphs.

## 🎯 Key Takeaways
- net/http/pprof captures non-invasive execution profiles of running production Go microservices
- Flamegraphs visualize hierarchical call stacks, highlighting functions consuming disproportionate CPU time
- Write statistical microbenchmarks with testing.B to verify that optimizations produce verifiable gains

## 🔍 Topics & Keywords
- `pprof Go tutorial`
- `Go flamegraph CPU profiling`
- `microbenchmarking testing.B Golang`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
