"""
Google Gemini integration for the RAG Chatbot System.
"""
import logging
from typing import List, Dict
import google.generativeai as genai
from models.document import SearchResult

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GeminiService:
    """Service for managing Google Gemini API interactions."""

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable must be set")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_response(self, query: str, context: List[SearchResult]) -> str:
        """Generate a response based on the query and provided context."""
        # Prepare context for the model
        context_text = "\n\n".join([f"Document {i+1}: {result.content}"
                                   for i, result in enumerate(context)])

        # Create the prompt with context
        prompt = f"""
        You are a helpful assistant that answers questions based only on the provided documentation.
        Do not use any external knowledge or make up information.

        Context from documentation:
        {context_text}

        Question: {query}

        Please provide an accurate answer based only on the provided documentation.
        If the answer cannot be found in the documentation, please say so clearly.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error generating response from Gemini: {e}")
            return "Sorry, I encountered an error while processing your request."

    def validate_context_relevance(self, query: str, response: str, context: List[SearchResult]) -> bool:
        """Validate that the response is relevant to the provided context."""
        # Implementation will be enhanced in later phases
        return True