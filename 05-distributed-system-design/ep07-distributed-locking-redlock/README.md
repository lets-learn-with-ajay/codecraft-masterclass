# Episode 07: Distributed Locking & Consensus: Redlock vs Raft/Zookeeper

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Preventing race conditions across distributed microservices using Redis Redlock, fencing tokens, and leader election consensus protocols.

## 🎯 Key Takeaways
- Simple single-node distributed locks fail silently during node crashes or asynchronous network partitions.
- Redlock acquires locks across N independent Redis master instances using quorum consensus.
- Fencing tokens (monotonically incrementing integers) protect backend storage and APIs from delayed client race conditions.

## 🔍 Topics Covered
- `Redis Redlock distributed locking`
- `fencing tokens distributed systems`

## 🚀 How to Run

```bash
python simulation.py
```
