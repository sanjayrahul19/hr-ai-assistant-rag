from src.rag.embedding_model import get_embedding_model


def test_embedding_model():
    embeddings = get_embedding_model()

    vector = embeddings.embed_query(
        "How many casual leave days are available?"
    )

    print("Vector dimensions:", len(vector))
    print("First 5 values:", vector[:5])


if __name__ == "__main__":
    test_embedding_model()
