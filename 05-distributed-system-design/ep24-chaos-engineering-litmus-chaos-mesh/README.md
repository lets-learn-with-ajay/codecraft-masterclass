# Episode 24: Chaos Engineering: Injecting Network Partitions, Packet Loss & Latency with Chaos Mesh

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Proving resilience before production outages. Setting up automated chaos engineering experiments: simulating split-brain network partitions, DNS failures, and node panics using Chaos Mesh and Litmus.

## 🎯 Key Takeaways
- Distributed systems are guaranteed to experience unexpected network partitions and hardware failures
- Chaos engineering deliberately injects failures in staging environments to verify automated failover behavior
- Automate experiments to prove that Raft clusters maintain quorums and circuit breakers trip as designed

## 🔍 Topics & Keywords
- `Chaos Mesh tutorial Kubernetes`
- `inject network partition chaos engineering`
- `Litmus chaos testing distributed systems`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
