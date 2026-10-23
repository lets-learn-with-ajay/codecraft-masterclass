# Episode 27: Automated RAG Hardening: Defending Against Prompt Injections & Poisoned Documents

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Securing retrieval against adversarial attacks. Detecting indirect prompt injections hidden in ingested PDFs, sanitizing instruction overrides, and enforcing strict data boundary delimiters.

## 🎯 Key Takeaways
- Untrusted third-party documents may contain hidden malicious instructions designed to hijack LLMs
- Pre-generation classifier models scan retrieved text for imperative command patterns and injection signatures
- Enforce strict XML-delimited prompt enclosures with system instructions instructing models to treat context as data only

## 🔍 Topics & Keywords
- `indirect prompt injection RAG`
- `defend against poisoned documents`
- `RAG security guardrails`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
