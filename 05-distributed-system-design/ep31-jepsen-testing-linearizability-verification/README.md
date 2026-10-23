# Episode 31: Jepsen Testing: Black-Box Verification of Linearizability & Partition Resilience in Distributed DBs

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Catching impossible bugs. Using Jepsen to inject network splits, clock jumps, and process pauses while verifying linearizable consistency against Knossos and Elle verification checkers.

## 🎯 Key Takeaways
- Jepsen tests simulate real-world catastrophic failure modes while running concurrent read/write workloads
- Knossos and Elle mathematical checkers analyze execution histories to detect consistency violations
- Uncovers subtle data loss, split-brain, and phantom read bugs that standard unit tests never reveal

## 🔍 Topics & Keywords
- `Jepsen testing tutorial`
- `linearizability verification Jepsen`
- `Knossos Elle consistency checking`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
