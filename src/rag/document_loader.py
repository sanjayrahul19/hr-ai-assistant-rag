import logging
from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document

logger=logging.getLogger(__name__)


def load_handbook_documents(pdf_path: str | Path) -> list[Document]:
     """
    Extract text from an employee handbook PDF.

    Returns one LangChain Document per non-empty PDF page.
    """
     
     file_path = Path(pdf_path)
     
     if not file_path.exists():
        raise FileNotFoundError(
            f"Handbook PDF not found: {file_path}"
        )
     
     if not file_path.is_file():
         raise ValueError(f"Expected a PDF file, got: {file_path}")
     
     if file_path.suffix.lower() != ".pdf":
         raise ValueError("Only PDF files are supported")
     
     try:
         reader=PdfReader(str(file_path))

         if reader.is_encrypted:
             raise ValueError("The handbook PDF is encrypted")
         
         documents=[]

         for page_number,page in enumerate(reader.pages, start=1):
             page_text=page.extract_text() or ""
             page_text=page_text.strip()

             if not page_text:
                 logger.warning(
                    "Skipping empty PDF page: %s",
                    page_number,
                )
                 continue
             
             document=Document(page_content=page_text,metadata={
                 "source":file_path.name,
                 "page":page_number
             })

             documents.append(document)


         if not documents:
            raise ValueError(
                "No extractable text found in the handbook PDF."
            )
         
         logger.info(
            "Loaded %s pages from %s",
            len(documents),
            file_path.name,
        )

         return documents       

     except ValueError:
         raise
     except Exception as exc:
         logger.exception("failed to read handbook PDF")
         raise RuntimeError("Could not extract text from the handbook PDF.") from exc

     
         

    


