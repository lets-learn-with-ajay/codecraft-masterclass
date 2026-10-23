# Episode 35: System Design Capstone (Part 3): Global Payment Engine — Multi-Region Active-Active & Disaster Failover

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Series Capstone Grand Finale: Achieving 99.999% availability. Architecting multi-region active-active database replication, automated DNS failover, zero-data-loss RPO, and sub-30s RTO recovery.

## 🎯 Key Takeaways
- Active-Active multi-region replication routes customer payments to the closest regional cluster seamlessly
- Quorum-based consensus protocols prevent split-brain partition divergence across continents
- Automated health checks and BGP/DNS routing achieve zero-data-loss (RPO = 0) and sub-30-second failover (RTO < 30s)

## 🔍 Topics & Keywords
- `multi region active active payment engine`
- `disaster recovery 99.999 availability`
- `system design capstone finale`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
