# Episode 34: System Design Capstone (Part 2): Global Payment Engine — Distributed 2PC, Outbox & Idempotency

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Series Capstone: Zero double-charges. Implementing distributed idempotency keys, the Transactional Outbox pattern, and coordinated two-phase commit flows across external banking gateways.

## 🎯 Key Takeaways
- Client idempotency keys ensure network retry requests return the original result without re-charging cards
- Transactional Outbox atomically records payment state changes and outbound gateway messages within local DB transactions
- Message relay workers publish events to banking gateways with guaranteed at-least-once delivery

## 🔍 Topics & Keywords
- `payment idempotency key architecture`
- `transactional outbox payment engine`
- `prevent double charges distributed systems`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
