# Episode 33: Go Microservices Capstone (Part 1): Distributed Key-Value Engine — Storage Architecture & WAL

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Series Capstone: Building a distributed storage engine. Constructing a concurrent SkipList MemTable, appending sequential binary mutations to a Write-Ahead Log (WAL), and crash recovery.

## 🎯 Key Takeaways
- Write-Ahead Logs append transactions sequentially to disk, ensuring zero data loss on node crashes
- Concurrent SkipLists enable lock-free, ordered in-memory lookups and insertions with O(log N) complexity
- The recovery engine replays WAL logs on startup to reconstruct in-memory state after abrupt failures

## 🔍 Topics & Keywords
- `build key value store Go`
- `WAL implementation Golang`
- `SkipList memtable Go capstone`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
