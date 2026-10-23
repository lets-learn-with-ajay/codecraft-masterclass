# Episode 24: Writing a Custom Raft Consensus Node in Go: Leader Election, Heartbeats & Log Replication

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Implementing core distributed algorithms from scratch. Constructing a complete Raft state machine in Go: randomized election timers, RequestVote RPCs, AppendEntries heartbeats, and committed index advancement.

## 🎯 Key Takeaways
- Raft maintains identical, linearized state machine logs across independent cluster nodes
- Randomized election timeouts prevent split-vote deadlocks during leader failures
- Quorum validation ensures log entries are committed only after acknowledgment by a majority of peers

## 🔍 Topics & Keywords
- `Raft consensus implementation Go`
- `build Raft from scratch Golang`
- `distributed leader election Go`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
