# Episode 25: Distributed Tracing at Planetary Scale: OpenTelemetry Collector Topologies & Tail-Based Sampling

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLLRN-SC_xr2w)
[![Track: Modern Distributed System Design & Scalability](https://img.shields.io/badge/Track-05_distributed_system_design-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Observability without network collapse. Designing high-throughput OpenTelemetry collector topologies, tail-based sampling algorithms that preserve error traces while discarding 99% of healthy spans.

## 🎯 Key Takeaways
- Head-based sampling decides whether to sample a trace before knowing if it will result in an error
- Tail-based sampling buffers complete trace waterfalls in memory, retaining 100% of errors and slow requests
- Reduces distributed tracing network bandwidth and storage costs by over 90%

## 🔍 Topics & Keywords
- `OpenTelemetry tail based sampling`
- `distributed tracing at scale`
- `OpenTelemetry Collector topology`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
