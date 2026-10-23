# Episode 12: Building Custom FastMCP Servers in Python: STDIO vs SSE Transports

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Authoring enterprise-grade Model Context Protocol (MCP) servers with FastMCP. Exposing local SQL databases, file systems, and bash tools over STDIO and Server-Sent Events (SSE) transports with automated schema generation.

## 🎯 Key Takeaways
- FastMCP provides Pythonic decorators (@mcp.tool) for zero-boilerplate tool declaration
- STDIO transport is optimal for local agent processes; SSE enables remote networked tool execution
- LangGraph clients discover tool schemas and resource endpoints dynamically at runtime

## 🔍 Topics & Keywords
- `FastMCP python tutorial`
- `build MCP server python`
- `Model Context Protocol SSE transport`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
