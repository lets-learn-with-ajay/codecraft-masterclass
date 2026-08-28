# Episode 01: Database Scaling: Sharding, Consistent Hashing & Hotspot Defense

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: Distributed System Design](https://img.shields.io/badge/Track-05_Distributed_Systems-fb923c?style=for-the-badge)](../README.md)

## 📌 Summary
When read replicas are no longer enough. Horizontal database partitioning, shard key selection, and consistent hashing rings.

## 🎯 Key Takeaways
- Vertical database scaling hits hard hardware ceilings; sharding partitions data across independent cluster nodes.
- Consistent hashing minimizes data re-shuffling when dynamically adding or removing shard nodes.
- Virtual nodes prevent hotspot data skew on celebrity partition keys and uneven hash ranges.

## 🔍 Topics Covered
- `database sharding system design`
- `consistent hashing ring tutorial`

## 🚀 How to Run

```bash
python simulation.py
```
