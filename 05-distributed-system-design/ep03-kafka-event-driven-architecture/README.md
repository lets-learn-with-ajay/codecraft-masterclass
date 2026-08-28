# Episode 03: Event-Driven Architecture with Apache Kafka & Idempotency

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Decoupling microservices with Kafka partitions, consumer groups, dead letter queues, and exactly-once processing semantics.

## 🎯 Key Takeaways
- Partitions enable horizontal consumer concurrency while guaranteeing strict ordered processing within each partition key.
- Consumer groups track individual committed offsets without blocking other downstream subscribing services.
- Idempotency keys and transactional producer envelopes prevent duplicate side-effects during network retries.

## 🔍 Topics Covered
- `Kafka system design event driven`
- `Kafka consumer groups idempotency`

## 🚀 How to Run

```bash
python simulation.py
```
