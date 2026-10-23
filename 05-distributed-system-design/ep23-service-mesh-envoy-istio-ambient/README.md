# Episode 23: Service Mesh Architecture: Envoy Data Plane, mTLS, Sidecars & Istio Ambient Mesh

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Enterprise cloud networking. Decoupling routing, telemetry, and mutual TLS encryption from containers using Envoy proxy sidecars vs sidecarless eBPF ambient mesh architectures.

## 🎯 Key Takeaways
- Service meshes offload cross-cutting network concerns (mTLS, retries, rate limits, metrics) from application code
- Sidecar proxies introduce memory and latency overhead for every container in a Kubernetes pod
- Istio Ambient Mesh uses shared node-level ztunnels and L7 waypoints to deliver zero-trust security without sidecars

## 🔍 Topics & Keywords
- `service mesh Envoy Istio tutorial`
- `Istio Ambient mesh architecture`
- `mutual TLS microservices mTLS`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
