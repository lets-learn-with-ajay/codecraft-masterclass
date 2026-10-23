# Episode 11: The Consistency Spectrum: Linearizability, Sequential, Causal & Eventual Consistency

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Demystifying data consistency. Comparing consistency models across the CAP and PACELC theorems, mapping real-world databases (Cassandra vs Spanner vs MongoDB), and trade-offs between latency and correctness.

## 🎯 Key Takeaways
- Linearizability guarantees that every read returns the most recent write in global physical time
- The PACELC theorem expands CAP: If Partition, choose Availability or Consistency; Else, choose Latency or Consistency
- Eventual consistency maximizes write throughput by sacrificing immediate cross-node read synchronization

## 🔍 Topics & Keywords
- `consistency models distributed systems`
- `PACELC theorem tutorial`
- `linearizability vs serializability`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
