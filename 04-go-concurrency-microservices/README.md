# ⚡ Track: High-Performance Go Microservices & Concurrency

> **Domain**: Backend Systems • **Tagline**: Master low-latency backend systems, Goroutines, gRPC, and production architecture

Official YouTube Playlist: [Watch Playlist](https://www.youtube.com/playlist?list=PLPHfa9OxyMCk)

## 📚 Episode Navigation & Curriculum

| Ep | Level | Title | Code |
|:--:|:-----:|-------|:----:|
| 01 | `BASIC` | The Go Concurrency Model Under the Hood: Goroutines & GMP | [`ep01-goroutines-gmp-scheduler`](ep01-goroutines-gmp-scheduler/) |
| 02 | `BASIC` | Robust Worker Pools & Fan-Out/Fan-In Pipeline Patterns | [`ep02-worker-pools-fanout-fanin`](ep02-worker-pools-fanout-fanin/) |
| 03 | `BASIC` | High-Throughput gRPC APIs with Protocol Buffers | [`ep03-grpc-protobuf-microservices`](ep03-grpc-protobuf-microservices/) |
| 04 | `BASIC` | Context Propagation, Cascading Timeouts & Graceful Deadlines | [`ep04-context-propagation-deadlines`](ep04-context-propagation-deadlines/) |
| 05 | `BASIC` | High-Concurrency PostgreSQL with pgx Connection Pooling | [`ep05-database-pooling-transactions`](ep05-database-pooling-transactions/) |
| 06 | `BASIC` | In-Memory Caching & Thundering Herd Defense with Singleflight | [`ep06-in-memory-caching-singleflight`](ep06-in-memory-caching-singleflight/) |
| 07 | `BASIC` | Production Observability: OpenTelemetry Tracing & Zero-Alloc slog | [`ep07-opentelemetry-distroless-docker`](ep07-opentelemetry-distroless-docker/) |
| 08 | `BASIC` | Resilient Microservices: Circuit Breakers, Retries & Jitter | [`ep08-circuit-breakers-resilience`](ep08-circuit-breakers-resilience/) |
| 09 | `BASIC` | Asynchronous Job Queues with Redis Streams & Worker Groups | [`ep09-async-job-queues-redis-streams`](ep09-async-job-queues-redis-streams/) |
| 10 | `BASIC` | 15MB Distroless Docker Builds & Kubernetes Graceful Shutdown | [`ep10-distroless-docker-k8s-graceful-shutdown`](ep10-distroless-docker-k8s-graceful-shutdown/) |
| 11 | `INTERMEDIATE` | Go 1.23+ Concurrency: Range-Over-Function Iterators (iter.Seq) in Concurrent Pipelines | [`ep11-go123-range-over-func-iterators`](ep11-go123-range-over-func-iterators/) |
| 12 | `INTERMEDIATE` | Lock-Free Programming: Atomic Primitives, Compare-And-Swap (CAS) & Memory Barriers | [`ep12-lock-free-atomics-cas`](ep12-lock-free-atomics-cas/) |
| 13 | `INTERMEDIATE` | High-Performance Lock-Free Ring Buffers & Disruptor Patterns in Go | [`ep13-lock-free-ring-buffers-disruptor`](ep13-lock-free-ring-buffers-disruptor/) |
| 14 | `INTERMEDIATE` | gRPC Bidirectional Streaming: Building a Real-Time High-Throughput Telemetry Service | [`ep14-grpc-bidirectional-streaming-telemetry`](ep14-grpc-bidirectional-streaming-telemetry/) |
| 15 | `INTERMEDIATE` | Concurrency with errgroup: Task Pipelines, Error Cancellation & SetLimit | [`ep15-errgroup-task-pipelines-rate-limits`](ep15-errgroup-task-pipelines-rate-limits/) |
| 16 | `INTERMEDIATE` | Event-Driven Microservices with NATS JetStream & Go: Ultra-Low Latency Pub/Sub | [`ep16-event-driven-nats-jetstream`](ep16-event-driven-nats-jetstream/) |
| 17 | `INTERMEDIATE` | High-Throughput WebSockets with Epoll: Scaling 1,000,000 Concurrent Connections with gnet | [`ep17-high-throughput-websockets-gnet`](ep17-high-throughput-websockets-gnet/) |
| 18 | `INTERMEDIATE` | Zero-Allocation Serialization: Replacing JSON with FlatBuffers, Cap'n Proto & Sonic | [`ep18-zero-alloc-serialization-flatbuffers-sonic`](ep18-zero-alloc-serialization-flatbuffers-sonic/) |
| 19 | `INTERMEDIATE` | Distributed Tracing with OpenTelemetry & W3C TraceContext Propagation across HTTP & gRPC | [`ep19-opentelemetry-w3c-tracecontext-propagation`](ep19-opentelemetry-w3c-tracecontext-propagation/) |
| 20 | `INTERMEDIATE` | Memory Optimization & Garbage Collection Tuning: GOGC, GOMEMLIMIT & Avoiding Heap Escapes | [`ep20-gc-tuning-gogc-gomemlimit`](ep20-gc-tuning-gogc-gomemlimit/) |
| 21 | `INTERMEDIATE` | Connection Pooling & Multiplexing: Designing a Production HTTP/3 & TCP Connection Pool | [`ep21-connection-pooling-http3-multiplexing`](ep21-connection-pooling-http3-multiplexing/) |
| 22 | `INTERMEDIATE` | Go 1.24 Weak Pointers & The unique Package: High-Speed Interning & Memory Deduplication | [`ep22-go124-weak-pointers-unique-package`](ep22-go124-weak-pointers-unique-package/) |
| 23 | `ADVANCED` | Kernel-Level Observability: eBPF Microservice Tracing with Go and Cilium/ebpf | [`ep23-kernel-ebpf-microservice-tracing`](ep23-kernel-ebpf-microservice-tracing/) |
| 24 | `ADVANCED` | Writing a Custom Raft Consensus Node in Go: Leader Election, Heartbeats & Log Replication | [`ep24-writing-custom-raft-consensus-go`](ep24-writing-custom-raft-consensus-go/) |
| 25 | `ADVANCED` | Distributed Rate Limiting: Sliding Window Counter with Redis & Atomic Local Leaky Buckets | [`ep25-distributed-rate-limiting-redis-leaky-bucket`](ep25-distributed-rate-limiting-redis-leaky-bucket/) |
| 26 | `ADVANCED` | High-Performance Zero-Copy I/O: Kernel sendfile, splice, and io_uring in Go | [`ep26-zero-copy-io-sendfile-iouring`](ep26-zero-copy-io-sendfile-iouring/) |
| 27 | `ADVANCED` | Dynamic Worker Pool Scaling & Backpressure Throttling under Extreme Spikes | [`ep27-dynamic-worker-pool-backpressure`](ep27-dynamic-worker-pool-backpressure/) |
| 28 | `ADVANCED` | Microservice Service Discovery & Health Checking with HashiCorp Consul & gRPC Resolvers | [`ep28-service-discovery-consul-grpc-resolvers`](ep28-service-discovery-consul-grpc-resolvers/) |
| 29 | `ADVANCED` | CPU Profiling & Microbenchmarking: Finding Allocation Hotspots with pprof & Flamegraphs | [`ep29-cpu-profiling-pprof-flamegraphs`](ep29-cpu-profiling-pprof-flamegraphs/) |
| 30 | `ADVANCED` | Profile-Guided Optimization (PGO) in Go: Achieving 15% Free Throughput Gains | [`ep30-profile-guided-optimization-pgo`](ep30-profile-guided-optimization-pgo/) |
| 31 | `ADVANCED` | Graceful Failover & Leader Election with etcd Leases in Distributed Go Microservices | [`ep31-leader-election-etcd-leases`](ep31-leader-election-etcd-leases/) |
| 32 | `ADVANCED` | Building a Distributed Lock Manager with Fencing Tokens in Go | [`ep32-distributed-lock-manager-fencing-tokens`](ep32-distributed-lock-manager-fencing-tokens/) |
| 33 | `ADVANCED` | Go Microservices Capstone (Part 1): Distributed Key-Value Engine — Storage Architecture & WAL | [`ep33-go-capstone-storage-wal-memtable`](ep33-go-capstone-storage-wal-memtable/) |
| 34 | `ADVANCED` | Go Microservices Capstone (Part 2): Distributed Key-Value Engine — Raft Consensus & Cluster Replication | [`ep34-go-capstone-raft-cluster-replication`](ep34-go-capstone-raft-cluster-replication/) |
| 35 | `ADVANCED` | Go Microservices Capstone (Part 3): Distributed Key-Value Engine — gRPC Gateway & Benchmarking | [`ep35-go-capstone-grpc-gateway-benchmarking`](ep35-go-capstone-grpc-gateway-benchmarking/) |

---

## 🚀 How to Use
Each episode folder contains runnable production source code, configuration files, and architectural diagrams.
Navigate to any episode subfolder and follow the local instructions.

```bash
cd 04-go-concurrency-microservices/ep01-*/
```
