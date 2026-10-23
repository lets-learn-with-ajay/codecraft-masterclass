# Episode 22: Asynchronous Agent Queueing & Concurrency Control with Redis & Celery

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Managing high-volume agent traffic. Decoupling HTTP API endpoints from long-running LangGraph agent executions using Redis message brokers, Celery worker pools, and task status polling.

## 🎯 Key Takeaways
- FastAPI endpoints return 202 Accepted with task IDs while Celery workers execute graphs asynchronously
- Redis tracks live agent lifecycle events and intermediate stream tokens for WebSocket broadcast
- Prevents serverless HTTP connection timeouts during 60+ second agent reasoning runs

## 🔍 Topics & Keywords
- `LangGraph Celery worker queue`
- `asynchronous AI agent Redis`
- `scaling LangGraph concurrency`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
