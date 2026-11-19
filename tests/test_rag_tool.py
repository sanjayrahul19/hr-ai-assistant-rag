
from src.rag.rag_tool import search_employee_handbook


def test_handbook_tool():

    result = search_employee_handbook.invoke({
        "question": "How many casual leaves are allowed annually?"
    })

    print("\nRetrieved handbook information:")
    print(result)


if __name__ == "__main__":
    test_handbook_tool()
