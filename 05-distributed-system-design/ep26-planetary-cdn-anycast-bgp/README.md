# Episode 26: Designing Planetary-Scale CDNs: Anycast BGP Routing, Edge PoPs & Sub-Second Invalidation

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Delivering content at lightspeed. Anycast BGP routing, peering at Internet Exchange Points (IXPs), multi-tier cache hierarchies (L1 edge, L2 regional shield), and instant cache purge propagation.

## 🎯 Key Takeaways
- Anycast BGP announces identical IP addresses globally, routing user packets to the topologically closest PoP
- Origin shield caches consolidate cache misses from hundreds of edge nodes, protecting origin backends
- Publish/subscribe invalidation backplanes propagate purge commands to global edge nodes within 150 milliseconds

## 🔍 Topics & Keywords
- `CDN system design Anycast BGP`
- `edge PoP architecture CDN`
- `sub second cache invalidation`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
