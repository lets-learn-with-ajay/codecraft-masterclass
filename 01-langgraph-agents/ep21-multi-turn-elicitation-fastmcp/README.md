# Episode 21: Multi-Turn Elicitation & Mid-Call User Clarification Flows with FastMCP

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Handling ambiguous tool arguments gracefully. Implementing interactive elicitation flows where MCP servers request missing parameters from the user before executing destructive or high-value operations.

## 🎯 Key Takeaways
- Elicitation primitives pause tool execution to ask targeted clarification questions rather than guessing
- Integrates seamlessly with LangGraph interrupt mechanisms to persist execution state during user input
- Drastically reduces failed API calls and user frustration on complex multi-argument operations

## 🔍 Topics & Keywords
- `FastMCP elicitation flow`
- `interactive agent parameter prompt`
- `LangGraph mid-call human clarification`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
