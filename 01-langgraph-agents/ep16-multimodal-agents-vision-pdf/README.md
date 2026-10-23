# Episode 16: Multi-Modal Agents: Processing Images, PDFs & Vision Inputs inside Graph Nodes

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLE3OhONv2GM8)
[![Track: Autonomous AI Agents with LangGraph & MCP](https://img.shields.io/badge/Track-01_langgraph_agents-38bdf8?style=for-the-badge)](../README.md)
[![Level: INTERMEDIATE](https://img.shields.io/badge/Level-INTERMEDIATE-emerald?style=for-the-badge)](#)

## 📌 Summary
Building visual reasoning agents. Handling base64 image buffers, architectural blueprints, and scanned PDF documents inside LangGraph state nodes using Claude 3.7 Sonnet and GPT-4o vision capabilities.

## 🎯 Key Takeaways
- Standardize image payloads as structured multi-modal content parts within HumanMessage objects
- Implement client-side downsampling and token estimation to prevent context window overflow
- Vision nodes can route dynamically to specialized code or OCR sub-agents based on diagram complexity

## 🔍 Topics & Keywords
- `multimodal AI agent LangGraph`
- `vision agent python GPT 4o`
- `image processing LangGraph node`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
