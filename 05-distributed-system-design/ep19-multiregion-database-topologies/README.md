# Episode 19: Multi-Region Database Topologies: Active-Passive, Multi-Leader & Geo-Partitioned Sharding

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Minimizing global latency. Designing multi-region architectures: Active-Passive with read replicas, Multi-Leader with conflict detection, and Geo-Partitioning where data lives in the user's home region.

## 🎯 Key Takeaways
- Cross-continental round trips introduce 150–250ms of speed-of-light physical latency per write
- Geo-partitioning stores table rows on database nodes physically located in the user's geographic jurisdiction
- Satisfies strict data sovereignty regulations (GDPR) while delivering sub-10ms localized read and write speeds

## 🔍 Topics & Keywords
- `multi region database design`
- `geo partitioned sharding`
- `active active database topology`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
