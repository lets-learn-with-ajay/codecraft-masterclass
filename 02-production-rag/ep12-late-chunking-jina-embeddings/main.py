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
