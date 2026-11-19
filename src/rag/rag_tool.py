from langchain.tools import tool
from src.rag.retriever import get_retriever

retriever=get_retriever()

@tool
def search_employee_handbook(question:str)->str:
    """
    Search the employee handbook for HR policies,
    leave rules, working hours and employee benefits.
    """

    documents=retriever.invoke(question)

    if not documents:
        return "No relevant handbook information found."
    
    context="\n\n".join(
        f"Source:{document.metadata.get('source','unknown')}\n"
        f"Page:{document.metadata.get('page','unknown')}\n"
        f"Content:{document.page_content}"
        for document in documents
    )

    return context