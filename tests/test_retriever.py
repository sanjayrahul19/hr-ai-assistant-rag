
from src.rag.retriever import get_retriever


def test_retriever():
    retriever = get_retriever()

    question = "How many casual leaves can an employee take annually?"

    results = retriever.invoke(question)

    print("\nUser question:", question)
    print("\nRetrieved documents:", len(results))

    for index, document in enumerate(results, start=1):
        print(f"\n--- Result {index} ---")
        print("Content:", document.page_content)
        print("Metadata:", document.metadata)


if __name__ == "__main__":
    test_retriever()
