# Episode 27: Zero-Downtime Database Migrations: Blue-Green Data Sync, Expand-Contract Pattern & Ghost Writes

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Evolving schemas without maintenance windows. Executing zero-downtime database migrations on petabyte-scale tables using the Expand-Contract pattern, shadow writing, and backfilling.

## 🎯 Key Takeaways
- ALTER TABLE locks large production tables, causing cascading application timeouts and outages
- The Expand-Contract pattern adds new columns, supports dual writing across versions, and deprecates old fields gradually
- Ghost-writing tools (gh-ost / pt-online-schema-change) replicate writes via binlogs without acquiring table locks

## 🔍 Topics & Keywords
- `zero downtime database migration`
- `expand contract pattern database`
- `online schema change ghost writes`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
