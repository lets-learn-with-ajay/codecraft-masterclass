# 🏗️ Track 5: Modern Distributed System Design & Scalability

> **Master large-scale architecture, sharding, event-driven streaming, and caching**

[![YouTube Playlist](https://img.shields.io/badge/YouTube-Playlist-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Domain: System Architecture](https://img.shields.io/badge/Domain-System_Architecture-fb923c?style=for-the-badge)](#)

---

## 📖 Overview

In this masterclass track, you will learn the core principles of designing massive-scale, fault-tolerant **Distributed Systems**. From database sharding and consistent hashing to Kafka event-driven architectures, distributed transactions (Saga & Outbox), sliding-window rate limiters, Redlock consensus, API Gateway routing, and multi-region active-active disaster recovery, this track equips you with senior-level system design skills.

---

## 🗺️ Episodes & Roadmap

| Ep | Episode Title | Key Highlights | Code |
|:--:|---------------|----------------|:----:|
| **01** | [Database Scaling: Sharding, Consistent Hashing & Hotspot Defense](ep01-database-sharding-hotspots/) | Shard keys, virtual consistent hashing rings, hotspot mitigation | [📂 Code](ep01-database-sharding-hotspots/) |
| **02** | [Distributed Caching & Cache Stampede Defense with Redis](ep02-distributed-caching-xfetch/) | Write-through / cache-aside, probabilistic early expiration (XFetch) | [📂 Code](ep02-distributed-caching-xfetch/) |
| **03** | [Event-Driven Architecture with Apache Kafka & Idempotency](ep03-kafka-event-driven-architecture/) | Kafka partitions, consumer groups, idempotency keys, exactly-once | [📂 Code](ep03-kafka-event-driven-architecture/) |
| **04** | [Distributed Transactions: The Saga Pattern & Transactional Outbox](ep04-distributed-transactions-saga-outbox/) | Choreographed/orchestrated sagas, CDC / Transactional Outbox | [📂 Code](ep04-distributed-transactions-saga-outbox/) |
| **05** | [Distributed Rate Limiting: Token Bucket vs Sliding Window Log](ep05-distributed-rate-limiting/) | Redis Lua scripts, token buckets, sliding window rate limits | [📂 Code](ep05-distributed-rate-limiting/) |
| **06** | [Real-Time Chat & Notification Scaling: WebSockets + Redis Pub/Sub](ep06-realtime-chat-websockets/) | Connection managers, Redis pub/sub backplanes, socket clustering | [📂 Code](ep06-realtime-chat-websockets/) |
| **07** | [Distributed Locking & Consensus: Redlock vs Raft/Zookeeper](ep07-distributed-locking-redlock/) | Redis Redlock, fencing tokens, Raft consensus, leader election | [📂 Code](ep07-distributed-locking-redlock/) |
| **08** | [API Gateway Design: Reverse Proxies, SSL & Global Edge Routing](ep08-api-gateway-edge-routing/) | Reverse proxy architecture, TLS termination, Anycast CDN routing | [📂 Code](ep08-api-gateway-edge-routing/) |
| **09** | [High-Throughput Ingestion: LSM Trees, ClickHouse & Time-Series DBs](ep09-write-heavy-ingestion-lsm-trees/) | MemTables, SSTables, ClickHouse columnar storage for 1M events/sec | [📂 Code](ep09-write-heavy-ingestion-lsm-trees/) |
| **10** | [Disaster Recovery, Multi-Region Active-Active & Split-Brain Mitigation](ep10-disaster-recovery-active-active/) | Multi-region active-active replication, CRDTs, quorum DNS failover | [📂 Code](ep10-disaster-recovery-active-active/) |

---

## 🛠️ Tech Stack & Prerequisites

- **Streaming & Messaging**: Apache Kafka, Redis Pub/Sub, RabbitMQ
- **Databases & Storage**: PostgreSQL (Sharded), ClickHouse, Neo4j, Redis Cluster
- **Gateways & Proxies**: Envoy, NGINX, Cloudflare Anycast
- **Simulation & Visuals**: Python / Go simulation scripts, PlantUML / Mermaid diagrams

---

## ⚡ Quick Start

```bash
cd 05-distributed-system-design/ep01-database-sharding-hotspots
python simulation.py
```
