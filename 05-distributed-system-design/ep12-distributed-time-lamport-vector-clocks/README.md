# Episode 12: Distributed Time & Ordering: Physical Clocks, Lamport Timestamps & Vector Clocks

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Why physical clocks cannot be trusted in distributed systems. NTP clock drift, clock skew hazards, causal ordering with Lamport Timestamps, and detecting concurrent conflicting writes with Vector Clocks.

## 🎯 Key Takeaways
- Physical quartz clocks drift uncontrollably across different servers, making physical timestamps unsafe for ordering
- Lamport Timestamps define a partial ordering of events based on 'happens-before' causal relationships
- Vector Clocks detect whether two operations are causally related or occurred concurrently as a conflict

## 🔍 Topics & Keywords
- `Lamport timestamps tutorial`
- `vector clocks distributed systems`
- `NTP clock drift distributed systems`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
