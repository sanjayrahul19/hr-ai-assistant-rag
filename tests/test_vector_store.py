
from src.rag.document_loader import load_handbook_documents
from src.rag.text_splitter import create_text_chunks
from src.rag.vector_store import create_vector_store


def test_vector_store():
    # Step 1: Load PDF
    documents = load_handbook_documents(
        "data/handbook/employee_handbook.pdf"
    )

    # Step 2: Split into chunks
    chunks = create_text_chunks(documents)

    print("Total chunks:", len(chunks))

    # Step 3: Store chunks and embeddings in ChromaDB
    vector_store = create_vector_store(chunks)

    print("ChromaDB collection created successfully!")


if __name__ == "__main__":
    test_vector_store()
