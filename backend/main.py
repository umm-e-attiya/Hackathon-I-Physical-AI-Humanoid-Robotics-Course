from fastapi import FastAPI, HTTPException
from services.qdrant_service import QdrantService
from pydantic import BaseModel
from typing import List

app = FastAPI()
qdrant_service = QdrantService()  

class IngestResponse(BaseModel):
    detail: str

class AskRequest(BaseModel):
    prompt: str

class AskResponse(BaseModel):
    results: List[dict]

@app.post("/ingest", response_model=IngestResponse)
def ingest_docs():
    try:
        qdrant_service.ingest_md_files()
        return {"detail": "Ingestion successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask", response_model=AskResponse)
def ask_bot(request: AskRequest):
    try:
        results = qdrant_service.search_documents(request.prompt)
        return {"results": [r.__dict__ for r in results]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
