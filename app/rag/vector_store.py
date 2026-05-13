import chromadb
from app.rag.embedding import (get_embedding)
from sentence_transformers import SentenceTransformer

client=chromadb.PersistentClient(
    path="./chroma_db"
)
def get_collection(user_id):
    collection= client.get_or_create_collection(
        name=f"{user_id}"
    )
    return collection
embedding_model=SentenceTransformer(
    'all-MiniLM-L6-v2',
)

def add_chunks_to_vectorstore(
    chunks,
    user_id,
    source="unknown"
):

    collection = get_collection(user_id)

    for i, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.add(

            documents=[chunk],

            embeddings=[embedding],

            ids=[f"{user_id}_{i}"],

            metadatas=[
                {
                    "source": source,
                    "chunk_id": i
                }
            ]
        )
#创建合集collection

def search_chunks(
        query,
        user_id,
        top_k=3):
    collection = get_collection(user_id)
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embedding=[query_embedding],
        n_results=top_k
    )
#查询向量
    return results["documents"][0]