from fastapi import APIRouter
from services.qdrant_service import QdrantService
from services.embedding_service import EmbeddingService

router = APIRouter()

qdrant = QdrantService()
embedder = EmbeddingService()

@router.post("/search")
def search(payload: dict):
    query = payload.get("query")
    vector = embedder.generate_embedding(query)
    results = qdrant.search(vector)
    return {"results": results}
