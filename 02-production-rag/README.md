# 🔍 Track 2: Production RAG & GraphRAG from Scratch

> **Build hallucination-free retrieval systems with hybrid search, re-ranking, and knowledge graphs**

[![YouTube Playlist](https://img.shields.io/badge/YouTube-Playlist-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/playlist?list=PLBeEI7uMhZos)
[![Domain: AI Engineering](https://img.shields.io/badge/Domain-AI_Engineering-818cf8?style=for-the-badge)](#)

---

## 📖 Overview

This track is an advanced masterclass on engineering enterprise-grade **Retrieval-Augmented Generation (RAG)** and **GraphRAG** pipelines. Move beyond toy vector search to build zero-hallucination systems featuring semantic splitting, Reciprocal Rank Fusion (RRF), cross-encoder re-ranking, Anthropic contextual chunking, Leiden community graph algorithms, Corrective RAG (CRAG), and automated Ragas evaluations.

---

## 🗺️ Episodes & Roadmap

| Ep | Episode Title | Key Highlights | Code |
|:--:|---------------|----------------|:----:|
| **01** | [The Chunking Dilemma: Semantic Splitting & Hierarchical Retrieval](ep01-chunking-and-semantic-splitting/) | Semantic splitting, parent-document retriever, context preservation | [📂 Code](ep01-chunking-and-semantic-splitting/) |
| **02** | [Hybrid Search: Dense Vectors + Sparse BM25 + Reciprocal Rank Fusion](ep02-hybrid-search-rrf/) | Combining dense semantic search with BM25 keyword matching via RRF | [📂 Code](ep02-hybrid-search-rrf/) |
| **03** | [Cross-Encoder Re-Ranking & Context Compression](ep03-cross-encoder-reranking/) | Top-30 candidate filtering to top-3 high-density context chunks | [📂 Code](ep03-cross-encoder-reranking/) |
| **04** | [Query Transformation: Multi-Query, Sub-Question & HyDE](ep04-query-transformation-hyde/) | Hypothetical Document Embeddings (HyDE) and query decomposition | [📂 Code](ep04-query-transformation-hyde/) |
| **05** | [Contextual Retrieval: Anthropic Chunk Contextualization Pattern](ep05-contextual-retrieval-anthropic/) | Prepending LLM document summaries to chunks before indexing | [📂 Code](ep05-contextual-retrieval-anthropic/) |
| **06** | [Knowledge Graphs & GraphRAG: Extracting Entity-Relation Triplets](ep06-knowledge-graphs-triplet-extraction/) | Extracting (Subject, Predicate, Object) triplets to build Neo4j graphs | [📂 Code](ep06-knowledge-graphs-triplet-extraction/) |
| **07** | [Multi-Hop Reasoning & Community Detection with GraphRAG](ep07-multi-hop-reasoning-community-detection/) | Leiden community clustering on knowledge graphs for global answers | [📂 Code](ep07-multi-hop-reasoning-community-detection/) |
| **08** | [Corrective RAG (CRAG) & Self-RAG: Dynamic Web Search Fallback](ep08-corrective-rag-crag-self-rag/) | Retrieval grading nodes with automated search fallback (Tavily/DDG) | [📂 Code](ep08-corrective-rag-crag-self-rag/) |
| **09** | [Automated RAG Evaluation: Faithfulness, Relevance & Groundedness](ep09-automated-rag-eval-ragas/) | Automated CI/CD evaluation pipelines using Ragas & the RAG Triad | [📂 Code](ep09-automated-rag-eval-ragas/) |
| **10** | [Scaling Vector DBs: HNSW Parameter Tuning & Product Quantization](ep10-vector-db-scaling-hnsw-quantization/) | HNSW index tuning, scalar quantization, and sub-10ms latency | [📂 Code](ep10-vector-db-scaling-hnsw-quantization/) |

---

## 🛠️ Tech Stack & Prerequisites

- **Python**: 3.11+
- **Vector DBs & Search**: Qdrant, Chroma, Pinecone, BM25, PgVector
- **Graph DBs**: Neo4j, NetworkX, Leiden Algorithm
- **Evaluation**: Ragas, TruLens
- **Embedding & Reranking Models**: BAAI/bge-reranker, Cohere Rerank, OpenAI Embeddings

---

## ⚡ Quick Start

```bash
cd 02-production-rag/ep01-chunking-and-semantic-splitting
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
