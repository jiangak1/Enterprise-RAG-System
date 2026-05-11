import chromadb
from openai.types import embedding_model
from sentence_transformers import SentenceTransformer

client=chromadb.Client()
collection=client.create_collection("rag_collection")
embedding_model=SentenceTransformer(
    'all-MiniLM-L6-v2',
)
