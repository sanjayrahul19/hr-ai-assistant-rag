
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_text_chunks( documents: list[Document], chunk_size: int = 500, chunk_overlap: int = 100) -> list[Document]:
    """
    Split page-level documents into smaller text chunks.
    Original metadata is preserved in each chunk.
    """

    if not documents:
        raise ValueError("No documents provided for splitting.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = splitter.split_documents(documents)

    return chunks
