# Episode 28: Consensus Under Byzantine Faults: Byzantine Fault Tolerance (BFT) vs Crash Fault Tolerance (CFT)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
When nodes lie. Deconstructing the Byzantine Generals Problem: why BFT requires 3f + 1 nodes compared to 2f + 1 in Raft/Paxos, PBFT (Practical Byzantine Fault Tolerance), and blockchain consensus.

## 🎯 Key Takeaways
- Crash Fault Tolerance (CFT) assumes failed nodes stop communicating honestly; BFT assumes nodes may act maliciously
- BFT protocols require at least 3f + 1 total nodes to tolerate f arbitrary or malicious failures
- Essential for multi-party decentralized networks, cryptographic ledgers, and zero-trust cross-organizational clusters

## 🔍 Topics & Keywords
- `Byzantine Fault Tolerance tutorial`
- `BFT vs CFT consensus`
- `PBFT algorithm distributed systems`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
