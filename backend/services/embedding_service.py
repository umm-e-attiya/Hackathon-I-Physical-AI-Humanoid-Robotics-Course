"""
Deterministic Embedding Service for RAG Chatbot System.
"""
import logging
from typing import List
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmbeddingService:
    """
    Service for generating deterministic embeddings for testing.
    Each text generates a fixed embedding using a simple hash.
    """

    def __init__(self):
        logger.info("Initializing Embedding Service (deterministic placeholder)")
        self.embedding_dim = 768  # Fixed dimension

    def generate_embedding(self, text: str) -> List[float]:
        """
        Generate deterministic embedding for given text.
        """
        # Convert text to bytes and sum character codes
        seed = sum([ord(c) for c in text])
        rng = np.random.default_rng(seed)  # deterministic random generator
        embedding = rng.random(self.embedding_dim).astype(np.float32).tolist()
        logger.debug(f"Generated embedding for text of length {len(text)}")
        return embedding

    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a batch of texts."""
        return [self.generate_embedding(text) for text in texts]


