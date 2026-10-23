# Episode 30: Advanced LangSmith CI/CD: Automated Dataset Benchmarking & Regression Testing

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Automating agent quality control. Building GitHub Actions CI/CD pipelines that evaluate agent changes against curated golden benchmark datasets using LangSmith custom evaluators and cost tracking.

## 🎯 Key Takeaways
- Run automated regression test suites against golden datasets on every Git pull request
- Compute exact accuracy, tool call correctness, and latency deltas between model versions
- Block deployments automatically if evaluation scores drop below baseline quality gates

## 🔍 Topics & Keywords
- `LangSmith CI CD evaluation`
- `automated agent testing GitHub Actions`
- `prevent agent prompt regression`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
