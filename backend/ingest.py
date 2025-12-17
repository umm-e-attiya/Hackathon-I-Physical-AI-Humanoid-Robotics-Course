from fastapi import FastAPI, HTTPException
from services.qdrant_service import QdrantService
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
qdrant_service = QdrantService()  # Initialize once

@app.post("/ingest")
async def ingest_documents():
    try:
        qdrant_service.ingest_md_files(docs_folder="data/docs")
        return {"status": "success", "message": "Documents ingested successfully"}
    except Exception as e:
        logger.error(f"Error during document ingestion: {e}")
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")
