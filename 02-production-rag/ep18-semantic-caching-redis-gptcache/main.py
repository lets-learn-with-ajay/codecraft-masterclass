# Phase 1: Semantic Chunking & Similarity Thresholds
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
# Split text dynamically based on sentence embedding gradient deltas
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type='percentile',
    breakpoint_threshold_amount=95
)
chunks = text_splitter.create_documents([raw_knowledge_base_text])

# Phase 2: Hierarchical Parent-Document Retrieval
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_community.vectorstores import Chroma

docstore = InMemoryStore()
vectorstore = Chroma(collection_name='parent_docs', embedding_function=embeddings)
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter
)
retrieved_parents = retriever.invoke('Explain state machine rollback invariants')

# Phase 2: Hierarchical Parent-Document Retrieval
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_community.vectorstores import Chroma

docstore = InMemoryStore()
vectorstore = Chroma(collection_name='parent_docs', embedding_function=embeddings)
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter
)
retrieved_parents = retriever.invoke('Explain state machine rollback invariants')

# Phase 1: Semantic Chunking & Similarity Thresholds
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
# Split text dynamically based on sentence embedding gradient deltas
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type='percentile',
    breakpoint_threshold_amount=95
)
chunks = text_splitter.create_documents([raw_knowledge_base_text])

# Phase 2: Hierarchical Parent-Document Retrieval
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_community.vectorstores import Chroma

docstore = InMemoryStore()
vectorstore = Chroma(collection_name='parent_docs', embedding_function=embeddings)
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter
)
retrieved_parents = retriever.invoke('Explain state machine rollback invariants')

# Phase 2: Hierarchical Parent-Document Retrieval
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_community.vectorstores import Chroma

docstore = InMemoryStore()
vectorstore = Chroma(collection_name='parent_docs', embedding_function=embeddings)
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter
)
retrieved_parents = retriever.invoke('Explain state machine rollback invariants')

# Phase 1: Semantic Chunking & Similarity Thresholds
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
# Split text dynamically based on sentence embedding gradient deltas
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type='percentile',
    breakpoint_threshold_amount=95
)
chunks = text_splitter.create_documents([raw_knowledge_base_text])
