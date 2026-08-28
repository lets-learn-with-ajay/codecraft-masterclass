# Episode 10: 15MB Distroless Docker Builds & Kubernetes Graceful Shutdown

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Go Concurrency & Microservices](https://img.shields.io/badge/Track-04_Go_Microservices-00ADD8?style=for-the-badge)](../README.md)

## 📌 Summary
Packaging Go microservices into minimal 15MB distroless scratch containers and implementing OS signal handling for zero-downtime K8s rolling deploys.

## 🎯 Key Takeaways
- Multi-stage Docker builds produce secure, minimal ~15MB production images with zero OS shell vulnerabilities.
- Trap `SIGTERM`/`SIGINT` signals to allow in-flight HTTP/gRPC requests to complete before process exit.
- Coordinate the application shutdown sequence with Kubernetes readiness probes for zero dropped client packets.

## 🔍 Topics Covered
- `minimal Go Docker scratch container`
- `Go graceful shutdown kubernetes SIGTERM`

## 🚀 How to Run

```bash
docker build -t go-microservice .
docker run -p 8080:8080 go-microservice
```
