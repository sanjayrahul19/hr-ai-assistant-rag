
from src.rag.document_loader import load_handbook_documents
from src.rag.text_splitter import create_text_chunks


def test_document_splitting():

    # Step 1: Load PDF pages
    documents = load_handbook_documents(
        "data/handbook/employee_handbook.pdf"
    )

    print("\nOriginal documents:", len(documents))

    # Step 2: Split documents into chunks
    chunks = create_text_chunks(
        documents,
        chunk_size=500,
        chunk_overlap=100,
    )

    print("Total chunks created:", len(chunks))

    # Step 3: Inspect the first chunk
    print("\nFirst chunk:")
    print(chunks[0].page_content)

    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

    # Step 4: Inspect all chunk sizes
    print("\nChunk sizes:")

    for index, chunk in enumerate(chunks, start=1):
        print(
            f"Chunk {index}: "
            f"{len(chunk.page_content)} characters"
        )


if __name__ == "__main__":
    test_document_splitting()
