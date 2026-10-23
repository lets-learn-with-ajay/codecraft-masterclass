# Episode 14: Conflict-Free Replicated Data Types (CRDTs): State-Based vs Operation-Based Resolution

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Mathematical conflict resolution without locks. Designing collaborative multi-region systems with CRDTs: PN-Counters, LWW-Element-Sets, and text sequence CRDTs (RGA/Yata) for collaborative editors.

## 🎯 Key Takeaways
- CRDTs guarantee that multiple replicas converge to identical states regardless of message order or duplicates
- State-based CRDTs (CvRDT) merge full replica payloads using mathematically commutative and idempotent join operations
- Operation-based CRDTs (CmRDT) transmit lightweight mutation operations over reliable delivery channels

## 🔍 Topics & Keywords
- `CRDT tutorial distributed systems`
- `conflict free replicated data types`
- `state based vs op based CRDT`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
