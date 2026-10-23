# Episode 24: Multi-Tenant Agent Isolation: Tenant Scoping, Row-Level Security & RBAC

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Zero data leakage in multi-user deployments. Enforcing tenant isolation in checkpointer databases, Row-Level Security (RLS) policies, and role-based tool execution authorization in LangGraph.

## 🎯 Key Takeaways
- Scope thread IDs and memory namespaces by tenant_id:user_id:session_id to prevent cross-talk
- Enforce PostgreSQL Row-Level Security on all checkpointer and vector store tables
- Tool execution middleware validates user JWT permissions before triggering privileged MCP tools

## 🔍 Topics & Keywords
- `multi tenant AI agent isolation`
- `LangGraph RBAC tool authorization`
- `Row Level Security AI agent`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
