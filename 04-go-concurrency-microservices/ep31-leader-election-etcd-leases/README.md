# Episode 31: Graceful Failover & Leader Election with etcd Leases in Distributed Go Microservices

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Active-passive high availability. Implementing distributed leader election using etcd key leases, automated heartbeat renewal, and sub-second failover when primary nodes crash.

## 🎯 Key Takeaways
- etcd leases automatically revoke leader keys if the active leader fails to renew heartbeats within TTL
- Standby nodes watch leader keys and trigger instantaneous elections upon key deletion
- Guarantees that exactly one instance executes singleton background tasks across a distributed cluster

## 🔍 Topics & Keywords
- `etcd leader election Go`
- `distributed lock etcd lease`
- `high availability failover Golang`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
