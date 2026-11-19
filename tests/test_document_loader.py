
from src.rag.document_loader import load_handbook_documents


def test_load_handbook():
    documents = load_handbook_documents(
        "data/handbook/employee_handbook.pdf"
    )

    print("Total documents:", len(documents))
    print("\nFirst document:")
    print(documents[0])


if __name__ == "__main__":
    test_load_handbook()
