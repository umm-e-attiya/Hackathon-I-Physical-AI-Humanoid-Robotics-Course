"""
Query request/response models for the RAG Chatbot System.
"""
from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    """Model representing a query request."""
    query: str
    max_results: int = 5
    context_window: Optional[str] = None

class QueryResponse(BaseModel):
    """Model representing a query response."""
    query: str
    response: str
    sources: List[str] = []
    context_used: List[dict] = []
    timestamp: str

class HealthCheckResponse(BaseModel):
    """Model representing a health check response."""
    status: str = "healthy"
    timestamp: str