# Episode 09: Asynchronous Job Queues with Redis Streams & Worker Groups

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Go Concurrency & Microservices](https://img.shields.io/badge/Track-04_Go_Microservices-00ADD8?style=for-the-badge)](../README.md)

## 📌 Summary
Building reliable asynchronous background workers in Go with Redis Streams consumer groups, Pending Entry List (PEL) acknowledgment, and DLQ recovery.

## 🎯 Key Takeaways
- Redis Streams provide ordered, append-only persistent message logs with scale-out consumer groups.
- The Pending Entry List (PEL) tracks unacknowledged jobs during unexpected worker crashes.
- Dead Letter Queues (DLQ) isolate poison-pill messages for manual inspection and alert notifications.

## 🔍 Topics Covered
- `Go Redis Streams consumer groups tutorial`
- `Golang background job queue Redis`

## 🚀 How to Run

```bash
go run main.go
```
