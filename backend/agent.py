"""
Central agent logic for the RAG Chatbot System.
This serves as the central brain that processes queries, searches documents,
selects context, and orchestrates response generation.
"""
import logging
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from config import settings
from models.document import SearchResult
from services.qdrant_service import QdrantService
from services.embedding_service import EmbeddingService
from services.gemini_service import GeminiService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Agent:
    """
    Central decision maker that processes queries, searches relevant docs,
    selects context, and orchestrates response generation.
    """

    def __init__(self):
        logger.info("Initializing RAG Chatbot Agent")

        # Initialize services
        self.qdrant_service = QdrantService(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
            api_key=settings.QDRANT_API_KEY
        )
        self.embedding_service = EmbeddingService()
        self.gemini_service = GeminiService(api_key=settings.GEMINI_API_KEY)

    def process_query(self, query: str, max_results: int = 5):
        """
        Process a user query and return a response based on document context.
        """
        logger.info(f"Processing query: {query}")

        try:
            # Generate embedding for the query
            query_embedding = self.embedding_service.generate_embedding(query)

            # Search relevant documents in Qdrant
            search_results = self.search_documents(query_embedding, max_results)

            # Generate response using Gemini based on context
            response = self.gemini_service.generate_response(query, search_results)

            # Return the response with context information
            result = {
                "query": query,
                "response": response,
                "sources": [result.metadata.get("source_file", "Unknown") for result in search_results],
                "context_used": [
                    {
                        "content": result.content[:200] + "..." if len(result.content) > 200 else result.content,
                        "score": result.score,
                        "source": result.metadata.get("source_file", "Unknown")
                    }
                    for result in search_results
                ]
            }

            return result

        except Exception as e:
            logger.error(f"Error processing query: {e}")
            return {
                "query": query,
                "response": f"Sorry, I encountered an error while processing your query: {str(e)}",
                "sources": [],
                "context_used": []
            }

    def search_documents(self, query_embedding: List[float], max_results: int = 5) -> List[SearchResult]:
        """
        Search relevant documents in the vector database.
        """
        logger.info(f"Searching documents with embedding of length {len(query_embedding) if query_embedding else 0}")

        try:
            search_results = self.qdrant_service.search_documents(query_embedding, limit=max_results)
            logger.info(f"Found {len(search_results)} relevant documents")
            return search_results
        except Exception as e:
            logger.error(f"Error searching documents: {e}")
            return []

    def select_context(self, query: str, search_results: List[SearchResult]):
        """
        Select relevant context from search results.
        This method is kept for compatibility but context selection is now handled
        within the process_query method.
        """
        return search_results

# Global agent instance
agent = Agent()

def get_agent():
    """Return the global agent instance."""
    return agent