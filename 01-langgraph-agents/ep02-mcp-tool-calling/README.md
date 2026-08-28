# Episode 02: Dynamic Tool Calling & Model Context Protocol (MCP)

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: LangGraph Agents](https://img.shields.io/badge/Track-01_LangGraph_Agents-38bdf8?style=for-the-badge)](../README.md)

## 📌 Summary
Standardizing agent tools with Anthropic's Model Context Protocol (MCP). Connecting an agent to local databases, filesystem utilities, and terminal execution tools.

## 🎯 Key Takeaways
- MCP eliminates custom bespoke API wrappers with a universal protocol for AI tool integration.
- `ToolNode` in LangGraph automatically handles tool execution and injects results back into graph state.
- Binding tools to chat models with strict JSON schema enforcement guarantees structured parameters.

## 🔍 Topics Covered
- `Model Context Protocol python tutorial`
- `LangGraph ToolNode MCP`
- `AI agent tool calling`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
