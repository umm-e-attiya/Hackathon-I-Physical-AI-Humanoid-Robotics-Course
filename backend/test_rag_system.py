"""
Simple test script to validate the RAG Chatbot System functionality.
"""
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_embedding_service():
    """Test the embedding service functionality."""
    print("Testing Embedding Service...")
    try:
        from services.embedding_service import EmbeddingService

        embedding_service = EmbeddingService()
        test_text = "This is a test sentence for embedding."
        embedding = embedding_service.generate_embedding(test_text)

        print(f"✓ Embedding generated successfully")
        print(f"  - Text length: {len(test_text)} characters")
        print(f"  - Embedding length: {len(embedding)} dimensions")
        print(f"  - Embedding type: {type(embedding)}")
        print(f"  - First 5 values: {embedding[:5]}")

        return True
    except Exception as e:
        print(f"✗ Error testing embedding service: {e}")
        return False

def test_qdrant_service():
    """Test the Qdrant service functionality."""
    print("\nTesting Qdrant Service...")
    try:
        from config import settings
        from services.qdrant_service import QdrantService

        qdrant_service = QdrantService(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
            api_key=settings.QDRANT_API_KEY
        )

        # Initialize collections
        qdrant_service.initialize_collections()
        print("✓ Qdrant collections initialized successfully")

        return True
    except Exception as e:
        print(f"✗ Error testing Qdrant service: {e}")
        return False

def test_agent_initialization():
    """Test the agent initialization."""
    print("\nTesting Agent Initialization...")
    try:
        from agent import Agent

        agent = Agent()
        print("✓ Agent initialized successfully")

        return True
    except Exception as e:
        print(f"✗ Error initializing agent: {e}")
        return False

def test_document_ingestion():
    """Test document ingestion functionality."""
    print("\nTesting Document Ingestion...")
    try:
        from ingest import ingest_documents

        # This will process the documents in data/docs/
        print("✓ Document ingestion function loaded successfully")
        print("  (Documents will be ingested when function is called)")

        return True
    except Exception as e:
        print(f"✗ Error with document ingestion: {e}")
        return False

def main():
    """Run all tests."""
    print("RAG Chatbot System - Validation Tests")
    print("=" * 50)

    tests = [
        test_embedding_service,
        test_qdrant_service,
        test_agent_initialization,
        test_document_ingestion
    ]

    results = []
    for test in tests:
        results.append(test())

    print("\n" + "=" * 50)
    print("Test Summary:")
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("✓ All tests passed! System is ready for use.")
        print("\nTo run the system:")
        print("1. Make sure Qdrant is running")
        print("2. Set your GEMINI_API_KEY in .env")
        print("3. Run: python -m uvicorn main:app --reload")
        print("4. Ingest documents: python ingest.py")
        print("5. Query the API at http://localhost:8000/query")
    else:
        print("✗ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()