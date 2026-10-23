# Episode 33: System Design Capstone (Part 1): Global Payment Engine — Ledger & Invariant Architecture

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Series Capstone: Building a mission-critical global payment processor. Designing an immutable double-entry financial ledger, database schema constraints, and sub-50ms transaction latency.

## 🎯 Key Takeaways
- Double-entry bookkeeping guarantees that every debit has an equal and opposite credit, preserving financial invariants
- Ledger entries are strictly immutable: adjustments are made through compensating reversal transactions only
- Database constraints and check clauses prevent account balances from slipping into invalid states

## 🔍 Topics & Keywords
- `payment engine system design`
- `double entry ledger architecture`
- `Stripe payment system design capstone`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
