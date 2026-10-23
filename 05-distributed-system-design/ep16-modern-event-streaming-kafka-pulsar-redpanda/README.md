# Episode 16: Modern Event Streaming: Apache Kafka vs Apache Pulsar vs Redpanda

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Architectural showdown: JVM partition logs (Kafka) vs decoupled compute-storage tiers with BookKeeper (Pulsar) vs C++ thread-per-core kernel bypass with tiered object storage (Redpanda).

## 🎯 Key Takeaways
- Kafka couples broker storage to local disk volumes, requiring expensive partition rebalancing upon scaling
- Pulsar decouples stateless brokers from BookKeeper storage, enabling independent compute and storage scaling
- Redpanda replaces the JVM with C++ and the Seastar framework, eliminating GC pauses and achieving 10x lower p99 latency

## 🔍 Topics & Keywords
- `Kafka vs Pulsar vs Redpanda`
- `Redpanda thread per core architecture`
- `event streaming architecture comparison`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
