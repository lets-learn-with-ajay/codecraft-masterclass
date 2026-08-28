# Episode 10: Disaster Recovery, Multi-Region Active-Active & Split-Brain Mitigation

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Designing mission-critical systems with multi-region active-active replication, conflict resolution (CRDTs), and split-brain mitigation.

## 🎯 Key Takeaways
- Active-Active architectures require clear write conflict resolution strategies (Conflict-Free Replicated Data Types - CRDTs or deterministic Last-Write-Wins timestamps).
- Quorum-based consensus protocols and odd-numbered voter nodes prevent split-brain partition divergence.
- Automated health probes and Anycast/DNS failover policies achieve RPO < 1s and RTO < 30s.

## 🔍 Topics Covered
- `multi region active active architecture`
- `disaster recovery split brain system design`

## 🚀 How to Run

```bash
python simulation.py
```
