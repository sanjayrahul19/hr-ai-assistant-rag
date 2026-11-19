from langchain_openai import OpenAIEmbeddings

from src.config import OPENAI_API_KEY, OPENAI_EMBEDDING_MODEL


def get_embedding_model():
     """Create and return the OpenAI embedding model."""

     embeddings=OpenAIEmbeddings(
          model=OPENAI_EMBEDDING_MODEL,
          api_key=OPENAI_API_KEY
     )

     return embeddings