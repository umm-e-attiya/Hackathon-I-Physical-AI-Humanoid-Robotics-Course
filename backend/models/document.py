"""
Document data models for the RAG Chatbot System.
"""
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Document(BaseModel):
    """Model representing a document."""
    id: str
    content: str
    metadata: dict = {}
    embedding: Optional[List[float]] = None
    created_at: datetime = datetime.now()
    source_file: Optional[str] = None

class DocumentChunk(BaseModel):
    """Model representing a chunk of a document."""
    id: str
    document_id: str
    content: str
    embedding: Optional[List[float]] = None
    chunk_index: int
    metadata: dict = {}

class SearchResult(BaseModel):
    """Model representing a search result from the vector database."""
    document_id: str
    content: str
    score: float
    metadata: dict = {}