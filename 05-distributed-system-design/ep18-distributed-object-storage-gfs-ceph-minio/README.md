# Episode 18: Distributed Object Storage: Architectural Deep Dive into Google File System (GFS), Ceph & MinIO

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Petabyte-scale storage engineering. Chunkserver layouts, master metadata scaling, erasure coding vs 3x replication, and CRUSH map data placement in Ceph and MinIO.

## 🎯 Key Takeaways
- Object stores separate metadata lookup servers from chunk/block data storage servers
- Erasure coding (e.g. Reed-Solomon 8+4) provides equal fault tolerance to 3x replication with 50% less raw disk storage
- Ceph's CRUSH algorithm computes object locations deterministically from metadata without requiring central lookup tables

## 🔍 Topics & Keywords
- `distributed object storage architecture`
- `Ceph CRUSH algorithm tutorial`
- `Google File System GFS architecture`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
