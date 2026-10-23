# Episode 34: Go Microservices Capstone (Part 2): Distributed Key-Value Engine — Raft Consensus & Cluster Replication

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Series Capstone: Replicating across nodes. Integrating the custom Raft consensus engine with the storage layer, cluster membership discovery, and automatic log replication across a 5-node cluster.

## 🎯 Key Takeaways
- Replicates client write mutations across a 5-node cluster before committing them to the local MemTable
- Node failures trigger automated term elections, electing a new leader within 150 milliseconds
- Linearizable read and write consistency guaranteed across network partitions

## 🔍 Topics & Keywords
- `distributed KV store Raft Go`
- `cluster replication Golang`
- `Raft state machine Go capstone`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
