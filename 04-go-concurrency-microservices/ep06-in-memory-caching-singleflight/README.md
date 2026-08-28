# Episode 06: In-Memory Caching & Thundering Herd Defense with Singleflight

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Go Concurrency & Microservices](https://img.shields.io/badge/Track-04_Go_Microservices-00ADD8?style=for-the-badge)](../README.md)

## 📌 Summary
Preventing cache stampedes in Go using `sync.Mutex`, `sync.RWMutex`, and `golang.org/x/sync/singleflight` duplicate call suppression.

## 🎯 Key Takeaways
- Singleflight guarantees that only one goroutine executes an expensive underlying query for identical concurrent keys.
- All concurrent duplicate requests pause and safely share the single returned result.
- Eliminates 99% of spike load on backend databases during high-traffic cache invalidations.

## 🔍 Topics Covered
- `Golang singleflight cache stampede`
- `Go concurrent in memory cache mutex`

## 🚀 How to Run

```bash
go run main.go
```
