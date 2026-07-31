from fastapi import APIRouter

from app.schemas.search import SearchRequest
from app.services.embedding.embedding_service import generate_embedding
from app.services.vector_store.chroma_service import search_similar_chunks

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.post("/")
def semantic_search(request: SearchRequest):

    embedding = generate_embedding(request.query)

    results = search_similar_chunks(
        embedding,
        request.n_results
    )

    return results