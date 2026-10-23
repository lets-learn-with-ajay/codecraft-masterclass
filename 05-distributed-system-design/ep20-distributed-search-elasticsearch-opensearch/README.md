# Episode 20: Distributed Search & Ingestion: Architectural Internals of Elasticsearch & OpenSearch Clusters

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Searching across petabytes. Shard routing, Lucene inverted indexes, segment merging, translog durability, and cluster rebalancing under heavy 100,000 docs/sec write workloads.

## 🎯 Key Takeaways
- Inverted indexes map terms to posting lists of matching document IDs for sub-millisecond keyword lookup
- Documents write to in-memory buffers and translogs first, periodically flushing immutable segment files
- Cluster master nodes monitor shard allocations and execute automated rebalancing during node failures

## 🔍 Topics & Keywords
- `Elasticsearch architecture internals`
- `OpenSearch cluster sharding`
- `Lucene inverted index segment merge`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
