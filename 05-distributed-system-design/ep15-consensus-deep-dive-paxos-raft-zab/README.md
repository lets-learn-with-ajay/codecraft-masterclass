# Episode 15: Distributed Consensus Deep Dive: Paxos vs Raft vs Zab (ZooKeeper Atomic Broadcast)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
The algorithmic foundation of distributed coordination. Comparative breakdown of Multi-Paxos, Raft leader terms, and ZooKeeper Atomic Broadcast (Zab), with quorum requirements and split-brain defenses.

## 🎯 Key Takeaways
- All consensus protocols require a majority quorum (N/2 + 1) of active nodes to guarantee progress without split-brain
- Paxos separates proposers and acceptors; Raft couples consensus directly to a strong leader state machine
- Zab is tailored specifically for primary-backup state replication and high-speed read-heavy workloads

## 🔍 Topics & Keywords
- `Paxos vs Raft vs Zab`
- `distributed consensus comparison`
- `ZooKeeper atomic broadcast Zab`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
