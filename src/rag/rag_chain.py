
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from src.config import OPENAI_API_KEY, OPENAI_MODEL
from src.rag.retriever import get_retriever


llm = ChatOpenAI(
    model=OPENAI_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=0
)

retriever = get_retriever()

prompt = ChatPromptTemplate.from_template("""
You are an HR assistant.

Answer using ONLY the provided context.
If the answer is unavailable, say the handbook does not provide it.

Context:
{context}

Question:
{question}
""")


def ask_hr_question(question: str):

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    formatted_prompt = prompt.invoke({
        "context": context,
        "question": question
    })

    response = llm.invoke(formatted_prompt)

    return response.content
