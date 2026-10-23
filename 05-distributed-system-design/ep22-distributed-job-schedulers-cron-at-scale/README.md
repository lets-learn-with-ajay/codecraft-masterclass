# Episode 22: Designing a Resilient Distributed Job Scheduler: Cron at Scale

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Executing millions of delayed and recurring jobs. Architecture of Uber Cherami and Airbnb Chronos: hierarchical time-wheel ring buffers, distributed lock leases, and exactly-once trigger guarantees.

## 🎯 Key Takeaways
- Single-server cron daemons cannot scale to millions of scheduled events and represent fatal single points of failure
- Hierarchical timing wheels schedule and advance millions of delayed timers in O(1) time complexity
- Fencing tokens and database leases prevent duplicate execution of high-value delayed jobs during failovers

## 🔍 Topics & Keywords
- `distributed job scheduler system design`
- `hierarchical timing wheels algorithm`
- `cron at scale system design`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
