# Episode 01: State Graphs vs Sequential Chains: LangGraph Core Primitives

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: LangGraph Agents](https://img.shields.io/badge/Track-01_LangGraph_Agents-38bdf8?style=for-the-badge)](../README.md)

## 📌 Summary
Why simple LLM chains fail on multi-step workflows. Building your first cyclic `StateGraph` with `TypedDict` state, node functions, and conditional routing edges.

## 🎯 Key Takeaways
- Sequential chains cannot handle cyclical loops, branching decisions, or self-correction.
- State is the single source of truth passed across all graph nodes.
- Conditional edges allow agents to dynamically branch based on LLM output and evaluation criteria.

## 🔍 Topics Covered
- `LangGraph StateGraph tutorial python`
- `LangGraph vs LangChain`
- `TypedDict state langgraph`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
