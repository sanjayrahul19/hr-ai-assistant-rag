from langchain_chroma import Chroma
from src.rag.embedding_model import get_embedding_model

def get_retriever():
    """Load the existing ChromaDB collection and return a retriever."""

    embeddings=get_embedding_model()

    vector_store=Chroma(
        collection_name='hr_handbook',
        embedding_function=embeddings,
        persist_directory="data/chroma_db"
    )

    retriever=vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":3}
    )

    return retriever