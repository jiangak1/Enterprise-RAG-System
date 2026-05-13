from app.rag.vector_store import search_chunks


def retrieve(query,user_id):
    results = search_chunks(query,user_id)
    return results