# Episode 01: The Go Concurrency Model Under the Hood: Goroutines & GMP

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Go Concurrency & Microservices](https://img.shields.io/badge/Track-04_Go_Microservices-00ADD8?style=for-the-badge)](../README.md)

## 📌 Summary
How Go handles 100,000 concurrent tasks on a single machine. The GMP scheduler, green threads, and dynamic stack growth.

## 🎯 Key Takeaways
- Goroutines start with only 2KB of stack space compared to 1-2MB OS threads, expanding dynamically.
- The GMP scheduler multiplexes M goroutines onto N OS threads across P logical processors.
- Work-stealing algorithms keep all CPU cores saturated without lock contention.

## 🔍 Topics Covered
- `Go GMP scheduler internals`
- `Goroutines vs OS threads Go tutorial`

## 🚀 How to Run

```bash
go run main.go
```
