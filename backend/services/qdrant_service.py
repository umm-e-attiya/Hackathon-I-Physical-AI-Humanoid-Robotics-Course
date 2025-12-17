import os
import uuid
import logging
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from services.embedding_service import EmbeddingService
from models.document import SearchResult

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QdrantService:
    VECTOR_DIM = 768
    COLLECTION_NAME = "docs"

    def __init__(self):
        # ❌ ENV variables ko hata diya, ab hardcoded
        host = "localhost"
        port = 6333
        api_key = None  # Agar API key chahiye toh yahan daal do

        try:
            self.client = QdrantClient(host=host, port=port, api_key=api_key)
            logger.info("Qdrant client initialized")
        except Exception as e:
            logger.error(f"Qdrant init failed: {e}")
            self.client = None

        self.embedding_service = EmbeddingService()

    def ingest_md_files(self, docs_folder: str = "data/docs"):
        if not self.client:
            raise RuntimeError("Qdrant client not initialized")

        # ---------- recreate collection ----------
        try:
            self.client.delete_collection(self.COLLECTION_NAME)
            logger.info("Old collection deleted")
        except Exception:
            logger.info("Collection did not exist")

        self.client.create_collection(
            collection_name=self.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=self.VECTOR_DIM,
                distance=Distance.COSINE,
            ),
        )
        logger.info("Collection created")

        if not os.path.exists(docs_folder):
            raise RuntimeError(f"Docs folder not found: {docs_folder}")

        for file_name in os.listdir(docs_folder):
            if not file_name.endswith(".md"):
                continue
            file_path = os.path.join(docs_folder, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            chunks = [text[i:i + 500] for i in range(0, len(text), 500)]
            for idx, chunk in enumerate(chunks):
                vector = self.embedding_service.generate_embedding(chunk)
                if len(vector) != self.VECTOR_DIM:
                    continue
                point = PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector,
                    payload={"content": chunk, "source": file_name, "chunk": idx},
                )
                self.client.upsert(
                    collection_name=self.COLLECTION_NAME,
                    points=[point],
                )
            logger.info(f"Ingested {file_name} ({len(chunks)} chunks)")

    def search_documents(self, query: str, limit: int = 5) -> List[SearchResult]:
        if not self.client:
            raise RuntimeError("Qdrant client not initialized")

        vector = self.embedding_service.generate_embedding(query)

        results = self.client.search(
            collection_name=self.COLLECTION_NAME,
            query_vector=vector,
            limit=limit,
        )

        return [
            SearchResult(
                document_id=r.payload.get("source", ""),
                content=r.payload.get("content", ""),
                score=r.score,
                metadata={"chunk": r.payload.get("chunk")},
            )
            for r in results
        ]
