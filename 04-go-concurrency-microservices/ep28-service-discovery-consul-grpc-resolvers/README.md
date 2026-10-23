# Episode 28: Microservice Service Discovery & Health Checking with HashiCorp Consul & gRPC Resolvers

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Track: High-Performance Go Microservices & Concurrency](https://img.shields.io/badge/Track-04_go_concurrency_microservices-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Dynamic client-side load balancing. Registering Go microservices with HashiCorp Consul, implementing custom gRPC name resolvers, and health check-driven traffic routing.

## 🎯 Key Takeaways
- Client-side load balancing routes RPCs directly to backend pods without central proxy bottlenecks
- Consul health check agents monitor pod availability and publish real-time catalog changes
- Custom gRPC resolvers dynamically update connection subchannels upon pod scaling events

## 🔍 Topics & Keywords
- `Consul service discovery Go`
- `custom gRPC resolver Golang`
- `client side load balancing gRPC`

## 🚀 How to Run

```bash
go mod tidy
go run main.go
```
