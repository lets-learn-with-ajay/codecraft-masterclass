# Phase 1: Candidate Generation & Cross-Encoder Initialization
from sentence_transformers import CrossEncoder

# Load high-accuracy cross-encoder for deep semantic re-scoring
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
candidate_docs = hybrid_retriever.get_relevant_documents(user_query, top_k=30)
pairs = [[user_query, doc.page_content] for doc in candidate_docs]
