from app.rag.vector_store import search_chunks
from app.core.logger import logger

def retrieve(query,user_id):
    logger.info(
        f"retrieval query: {query}"
    )
    results = search_chunks(query,user_id)
    logger.info(
        f"retrieved chunks: {results}"
    )
    return results