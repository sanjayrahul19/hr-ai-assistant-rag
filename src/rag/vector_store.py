from langchain_chroma import Chroma

from src.rag.embedding_model import get_embedding_model

def create_vector_store(chunks):
    """Store document chunks and their embeddings in ChromaDB."""

    embeddings = get_embedding_model()

    vector_store=Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name='hr_handbook',
        persist_directory="data/chroma_db"

    )
    
    return vector_store