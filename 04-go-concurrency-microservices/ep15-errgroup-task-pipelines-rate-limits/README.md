# Episode 15: Concurrency with errgroup: Task Pipelines, Error Cancellation & SetLimit

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Clean concurrent orchestration. Using golang.org/x/sync/errgroup to run bounded parallel workers, short-circuiting on first error, and enforcing strict concurrency limits with SetLimit.

## 🎯 Key Takeaways
- errgroup manages collections of goroutines, automatically propagating cancellation upon first error
- SetLimit restricts maximum active goroutines, preventing resource exhaustion on unbounded input sets
- Eliminates complex sync.WaitGroup + error channel coordination boilerplate entirely

## 🔍 Topics & Keywords
- `Golang errgroup tutorial`
- `errgroup SetLimit concurrency`
- `parallel task pipeline Go error handling`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
