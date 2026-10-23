# Episode 13: Google Spanner TrueTime & CockroachDB Hybrid Logical Clocks (HLC)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Engineering reliable global time. How Google Spanner uses GPS and atomic clocks to bound time uncertainty (TrueTime), and how CockroachDB implements Hybrid Logical Clocks (HLC) on commodity hardware.

## 🎯 Key Takeaways
- TrueTime represents time as an interval [earliest, latest] bounded by atomic clocks and GPS receivers
- Spanner achieves external consistency by waiting out the uncertainty interval before committing transactions
- Hybrid Logical Clocks combine physical time with logical counters to provide monotonic ordering without atomic hardware

## 🔍 Topics & Keywords
- `Google Spanner TrueTime tutorial`
- `Hybrid Logical Clocks HLC CockroachDB`
- `external consistency distributed DB`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
