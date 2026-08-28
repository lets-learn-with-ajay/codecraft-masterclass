# 🤖 Track 1: Autonomous AI Agents with LangGraph & MCP

> **Master stateful AI agents, human-in-the-loop controls, and Model Context Protocol**

[![YouTube Playlist](https://img.shields.io/badge/YouTube-Playlist-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/playlist?list=PLE3OhONv2GM8)
[![Domain: Generative AI](https://img.shields.io/badge/Domain-Generative_AI-38bdf8?style=for-the-badge)](#)

---

## 📖 Overview

In this masterclass track, you will learn how to build resilient, stateful multi-agent systems from the ground up using **LangGraph**, **LangChain**, and Anthropic's **Model Context Protocol (MCP)**. From cyclic state graphs to human-in-the-loop approval workflows, hierarchical agent teams, and production telemetry with LangSmith, this track covers everything required to deploy production-grade AI agents.

---

## 🗺️ Episodes & Roadmap

| Ep | Episode Title | Key Highlights | Code |
|:--:|---------------|----------------|:----:|
| **01** | [State Graphs vs Sequential Chains: LangGraph Core Primitives](ep01-state-graphs-vs-chains/) | Cyclic graphs, TypedDict state, conditional branching | [📂 Code](ep01-state-graphs-vs-chains/) |
| **02** | [Dynamic Tool Calling & Model Context Protocol (MCP)](ep02-mcp-tool-calling/) | Universal MCP tools, ToolNode, database/terminal connectors | [📂 Code](ep02-mcp-tool-calling/) |
| **03** | [Persistent Memory & Time-Travel Debugging with Checkpointers](ep03-memory-and-checkpointing/) | SqliteSaver / Postgres checkpointers, state rewinding | [📂 Code](ep03-memory-and-checkpointing/) |
| **04** | [Human-in-the-Loop: Dynamic Breakpoints & Approval Flows](ep04-human-in-the-loop/) | `interrupt_before`, state mutation, payment/action approval | [📂 Code](ep04-human-in-the-loop/) |
| **05** | [Multi-Agent Supervisors & Specialized Sub-Agents](ep05-multi-agent-supervisors/) | Supervisor router, specialized agents (researcher, coder, reviewer) | [📂 Code](ep05-multi-agent-supervisors/) |
| **06** | [Reflection & Self-Correction Loops with Automated Evaluators](ep06-reflection-self-correction/) | Critic/Evaluator nodes, syntax linter loops, self-healing code | [📂 Code](ep06-reflection-self-correction/) |
| **07** | [Hierarchical Multi-Agent Teams & Distributed State Delegation](ep07-hierarchical-multi-agent-teams/) | Nested subgraphs, team leads, local state scoping | [📂 Code](ep07-hierarchical-multi-agent-teams/) |
| **08** | [Agentic Streaming & Real-Time Event Emits (astream_events)](ep08-agentic-streaming-events/) | Token streaming, lifecycle events, live UI visualizers | [📂 Code](ep08-agentic-streaming-events/) |
| **09** | [Long-Term Memory & Entity Stores with Semantic Search](ep09-long-term-memory-entity-stores/) | Cross-thread memory, Mem0/Zep pattern, semantic extraction | [📂 Code](ep09-long-term-memory-entity-stores/) |
| **10** | [Production Deployment, LangSmith Tracing & Cost Guardrails](ep10-production-deployment-langsmith/) | FastAPI / LangGraph Server, trace trees, token budgets | [📂 Code](ep10-production-deployment-langsmith/) |

---

## 🛠️ Tech Stack & Prerequisites

- **Python**: 3.11+
- **Frameworks**: LangGraph, LangChain Core, LangSmith
- **Protocols**: Model Context Protocol (MCP)
- **Databases**: SQLite, PostgreSQL (for checkpointers)
- **LLM Providers**: OpenAI, Anthropic, Ollama (local)

---

## ⚡ Quick Start

Choose an episode directory and set up your Python virtual environment:

```bash
cd 01-langgraph-agents/ep01-state-graphs-vs-chains
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
