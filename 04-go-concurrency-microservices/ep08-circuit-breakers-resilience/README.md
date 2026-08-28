# Episode 08: Resilient Microservices: Circuit Breakers, Retries & Jitter

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Go Concurrency & Microservices](https://img.shields.io/badge/Track-04_Go_Microservices-00ADD8?style=for-the-badge)](../README.md)

## 📌 Summary
Implementing fault tolerance with Sony `GoBreaker`, exponential backoff algorithms, and randomized jitter to prevent cascading microservice failures.

## 🎯 Key Takeaways
- Circuit breakers fail-fast to prevent cascading outages and resource starvation across upstream microservices.
- Exponential backoff combined with full jitter distributes retry spikes across time.
- Clear state transitions (`Closed` -> `Open` -> `Half-Open`) shield recovering downstream dependencies.

## 🔍 Topics Covered
- `Golang circuit breaker pattern tutorial`
- `exponential backoff jitter Go`

## 🚀 How to Run

```bash
go run main.go
```
