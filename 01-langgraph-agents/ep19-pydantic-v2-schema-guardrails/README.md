# Episode 19: Pydantic v2 Output Validation & Strict Schema Guardrails in Node Execution

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Zero-error state contracts. Enforcing Pydantic v2 schema validation on intermediate agent node outputs, automatic validation error recovery loops, and deterministic downstream data consumption.

## 🎯 Key Takeaways
- Enforce strict typing at node boundaries using Pydantic v2 model_validate_json
- Route validation failures to self-healing retry nodes with formatted error diagnostics
- Guarantees that downstream business logic receives valid payloads with zero KeyError exceptions

## 🔍 Topics & Keywords
- `Pydantic v2 LangGraph output validation`
- `structured output agent guardrails`
- `LangGraph error retry node`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
