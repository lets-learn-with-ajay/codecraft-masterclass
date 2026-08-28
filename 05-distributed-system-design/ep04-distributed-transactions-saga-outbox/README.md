# Episode 04: Distributed Transactions: The Saga Pattern & Transactional Outbox

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
Maintaining data consistency across microservices without 2-phase commit (2PC) using Choreographed/Orchestrated Sagas and the Transactional Outbox Pattern.

## 🎯 Key Takeaways
- 2-Phase Commit (2PC) locks database resources across networks and introduces catastrophic single points of failure.
- Sagas break distributed transactions into atomic local transactions with corresponding compensating rollback actions.
- The Transactional Outbox pattern guarantees atomic local database mutations and dependable message publishing via CDC (Change Data Capture).

## 🔍 Topics Covered
- `Saga pattern distributed transactions`
- `Transactional outbox pattern microservices`

## 🚀 How to Run

```bash
python simulation.py
```
