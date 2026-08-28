# Episode 08: API Gateway Design: Reverse Proxies, SSL & Global Edge Routing

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Designing a high-throughput API Gateway layer for authentication, TLS termination, path routing, and global Anycast CDN edge acceleration.

## 🎯 Key Takeaways
- API Gateways decouple cross-cutting concerns (authentication, TLS offloading, rate limiting, logging) from core microservice logic.
- HTTP/3 (QUIC) and Anycast BGP routing minimize round-trip latency for global client requests.
- Dynamic upstream service discovery ensures seamless zero-downtime canary rollouts and blue-green deployments.

## 🔍 Topics Covered
- `API gateway system design Envoy`
- `reverse proxy edge routing microservices`

## 🚀 How to Run

```bash
python simulation.py
```
