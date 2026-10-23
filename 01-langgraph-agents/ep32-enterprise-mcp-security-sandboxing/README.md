# Episode 32: Enterprise MCP Security: Sandboxed Code Execution, Tool Authorization & Secret Redaction

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Hardening the agent attack surface. Preventing prompt injection tool misuse, redacting secrets and PII from execution logs, and running MCP tools inside gVisor/Docker micro-sandboxes.

## 🎯 Key Takeaways
- Isolate local tool execution inside sandboxed containers with read-only root filesystems
- Implement regex and NER scrubbing to redact API keys and PII before logging or sending upstream
- Enforce human confirmation barriers on irreversible operations (database drops, fund transfers)

## 🔍 Topics & Keywords
- `MCP security hardening`
- `prompt injection tool protection`
- `sandboxed AI agent execution`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
