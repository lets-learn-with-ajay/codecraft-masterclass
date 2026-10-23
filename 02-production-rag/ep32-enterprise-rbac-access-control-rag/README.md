# Episode 32: Enterprise Access Control & Document-Level RBAC in Retrieval Pipelines

[![Watch Video](https://img.shields.io/badge/YouTube-Watch%20Episode-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PLBeEI7uMhZos)
[![Track: Production RAG & GraphRAG from Scratch](https://img.shields.io/badge/Track-02_production_rag-38bdf8?style=for-the-badge)](../README.md)
[![Level: ADVANCED](https://img.shields.io/badge/Level-ADVANCED-emerald?style=for-the-badge)](#)

## 📌 Summary
Confidentiality and compliance. Propagating Active Directory/OAuth user roles into vector search filters, preventing unauthorized context leaks, and compliance auditing.

## 🎯 Key Takeaways
- Never allow LLMs to see retrieved documents that the requesting user does not have permission to view
- Embed user group ACLs into vector metadata and enforce hard boolean pre-filters at the database level
- Audit logs record the exact documents retrieved and verified against user security credentials

## 🔍 Topics & Keywords
- `document level RBAC RAG`
- `enterprise access control vector search`
- `Active Directory permission filter RAG`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```
