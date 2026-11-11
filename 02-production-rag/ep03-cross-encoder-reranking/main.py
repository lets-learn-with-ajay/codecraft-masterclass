# Phase 1: Candidate Generation & Cross-Encoder Initialization
from sentence_transformers import CrossEncoder

# Load high-accuracy cross-encoder for deep semantic re-scoring
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
candidate_docs = hybrid_retriever.get_relevant_documents(user_query, top_k=30)
pairs = [[user_query, doc.page_content] for doc in candidate_docs]

# Phase 2: Re-Ranking & Context Compression
scores = cross_encoder.predict(pairs)
scored_docs = sorted(zip(candidate_docs, scores), key=lambda x: x[1], reverse=True)
top_ranked = [doc for doc, score in scored_docs[:3]]
# Compress context into dense prompt buffer
compressed_context = '\n---\n'.join([d.page_content for d in top_ranked])

# Phase 2: Re-Ranking & Context Compression
scores = cross_encoder.predict(pairs)
scored_docs = sorted(zip(candidate_docs, scores), key=lambda x: x[1], reverse=True)
top_ranked = [doc for doc, score in scored_docs[:3]]
# Compress context into dense prompt buffer
compressed_context = '\n---\n'.join([d.page_content for d in top_ranked])

# Phase 1: Candidate Generation & Cross-Encoder Initialization
from sentence_transformers import CrossEncoder

# Load high-accuracy cross-encoder for deep semantic re-scoring
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
candidate_docs = hybrid_retriever.get_relevant_documents(user_query, top_k=30)
pairs = [[user_query, doc.page_content] for doc in candidate_docs]

# Phase 2: Re-Ranking & Context Compression
scores = cross_encoder.predict(pairs)
scored_docs = sorted(zip(candidate_docs, scores), key=lambda x: x[1], reverse=True)
top_ranked = [doc for doc, score in scored_docs[:3]]
# Compress context into dense prompt buffer
compressed_context = '\n---\n'.join([d.page_content for d in top_ranked])

# Phase 2: Re-Ranking & Context Compression
scores = cross_encoder.predict(pairs)
scored_docs = sorted(zip(candidate_docs, scores), key=lambda x: x[1], reverse=True)
top_ranked = [doc for doc, score in scored_docs[:3]]
# Compress context into dense prompt buffer
compressed_context = '\n---\n'.join([d.page_content for d in top_ranked])

# Phase 1: Candidate Generation & Cross-Encoder Initialization
from sentence_transformers import CrossEncoder

# Load high-accuracy cross-encoder for deep semantic re-scoring
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
candidate_docs = hybrid_retriever.get_relevant_documents(user_query, top_k=30)
pairs = [[user_query, doc.page_content] for doc in candidate_docs]
