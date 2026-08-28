# ⚡ Track 4: High-Performance Go Microservices & Concurrency

> **Master low-latency backend systems, Goroutines, gRPC, and production architecture**

[![YouTube Playlist](https://img.shields.io/badge/YouTube-Playlist-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/playlist?list=PLPHfa9OxyMCk)
[![Domain: Backend Systems](https://img.shields.io/badge/Domain-Backend_Systems-00ADD8?style=for-the-badge)](#)

---

## 📖 Overview

In this masterclass track, you will dive deep into high-performance backend engineering with **Go (Golang)**. Explore the internals of the GMP scheduler, master concurrent worker pools and fan-out/fan-in patterns, construct high-throughput gRPC services with Protocol Buffers, manage database connection pools with pgx, prevent cache stampedes with singleflight, and deploy minimal 15MB distroless containers on Kubernetes.

---

## 🗺️ Episodes & Roadmap

| Ep | Episode Title | Key Highlights | Code |
|:--:|---------------|----------------|:----:|
| **01** | [The Go Concurrency Model Under the Hood: Goroutines & GMP](ep01-goroutines-gmp-scheduler/) | GMP scheduler mechanics, work-stealing, 2KB green threads | [📂 Code](ep01-goroutines-gmp-scheduler/) |
| **02** | [Robust Worker Pools & Fan-Out/Fan-In Pipeline Patterns](ep02-worker-pools-fanout-fanin/) | Buffered channels, worker pools, fan-out/fan-in, context cancellation | [📂 Code](ep02-worker-pools-fanout-fanin/) |
| **03** | [High-Throughput gRPC APIs with Protocol Buffers](ep03-grpc-protobuf-microservices/) | Protobuf schema definitions, HTTP/2 multiplexing, streaming RPCs | [📂 Code](ep03-grpc-protobuf-microservices/) |
| **04** | [Context Propagation, Cascading Timeouts & Graceful Deadlines](ep04-context-propagation-deadlines/) | Cascading timeouts, dead-line propagation, preventing orphaned routines | [📂 Code](ep04-context-propagation-deadlines/) |
| **05** | [High-Concurrency PostgreSQL with pgx Connection Pooling](ep05-database-pooling-transactions/) | pgx connection pool tuning, atomic transactions, avoiding starvations | [📂 Code](ep05-database-pooling-transactions/) |
| **06** | [In-Memory Caching & Thundering Herd Defense with Singleflight](ep06-in-memory-caching-singleflight/) | Cache stampede prevention, sync.RWMutex, singleflight duplicate suppression | [📂 Code](ep06-in-memory-caching-singleflight/) |
| **07** | [Production Observability: OpenTelemetry Tracing & Zero-Alloc slog](ep07-opentelemetry-distroless-docker/) | Distributed tracing with OpenTelemetry, Prometheus metrics, structured slog | [📂 Code](ep07-opentelemetry-distroless-docker/) |
| **08** | [Resilient Microservices: Circuit Breakers, Retries & Jitter](ep08-circuit-breakers-resilience/) | Sony GoBreaker, exponential backoff with full randomized jitter | [📂 Code](ep08-circuit-breakers-resilience/) |
| **09** | [Asynchronous Job Queues with Redis Streams & Worker Groups](ep09-async-job-queues-redis-streams/) | Consumer groups, Pending Entry List (PEL), Dead Letter Queue (DLQ) | [📂 Code](ep09-async-job-queues-redis-streams/) |
| **10** | [15MB Distroless Docker Builds & Kubernetes Graceful Shutdown](ep10-distroless-docker-k8s-graceful-shutdown/) | Multi-stage distroless scratch builds, SIGTERM trapping, K8s probes | [📂 Code](ep10-distroless-docker-k8s-graceful-shutdown/) |

---

## 🛠️ Tech Stack & Prerequisites

- **Language**: Go 1.22+
- **RPC & Serialization**: gRPC, Protocol Buffers (protoc)
- **Database & Cache**: PostgreSQL (pgx/v5), Redis (go-redis/v9)
- **Observability**: OpenTelemetry Go SDK, Prometheus client, log/slog
- **Containerization**: Docker (Distroless / Scratch), Kubernetes

---

## ⚡ Quick Start

```bash
cd 04-go-concurrency-microservices/ep01-goroutines-gmp-scheduler
go run main.go
```
