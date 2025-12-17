"""
Configuration and environment management for the RAG Chatbot System.
"""
import os
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Qdrant configuration
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", "6333"))
    QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY")

    # Gemini configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    # Application configuration
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Collections
    DOCS_COLLECTION_NAME: str = os.getenv("DOCS_COLLECTION_NAME", "docs")
    SELECTED_DOCS_COLLECTION_NAME: str = os.getenv("SELECTED_DOCS_COLLECTION_NAME", "selected_docs")

    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()

def get_settings():
    """Return the global settings instance."""
    return settings