# Episode 03: Persistent Memory & Time-Travel Debugging with Checkpointers

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/PLACEHOLDER)
[![Track: LangGraph Agents](https://img.shields.io/badge/Track-01_LangGraph_Agents-38bdf8?style=for-the-badge)](../README.md)

## 📌 Summary
Saving and restoring agent execution states using `SqliteSaver` and Postgres checkpointers for production reliability and multi-session persistence.

## 🎯 Key Takeaways
- Checkpointers snapshot agent state at every superstep, enabling state persistence and recovery.
- Thread IDs isolate concurrent user conversation sessions across stateless web servers.
- Time-travel allows rewinding graph execution and modifying historical state to debug errors.

## 🔍 Topics Covered
- `LangGraph memory checkpointer`
- `SqliteSaver LangGraph tutorial`
- `time travel debugging AI agent`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
