# Episode 13: Integrating DeepSeek-R1 & OpenAI o3: Reasoning Chains in Agent State

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Architecting agents around reasoning models. Extracting and isolating <think> reasoning tokens from final tool calls, managing token budget overhead, and storing structured thought traces in LangGraph state.

## 🎯 Key Takeaways
- Reasoning models output internal thought traces that must be isolated from user-facing agent state
- Regex and streaming event interceptors prevent raw <think> blocks from polluting downstream tool inputs
- Persisting reasoning traces in checkpointer metadata enables post-execution algorithmic auditing

## 🔍 Topics & Keywords
- `DeepSeek R1 LangGraph`
- `OpenAI o3 reasoning agent`
- `reasoning tokens think tag langgraph`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
