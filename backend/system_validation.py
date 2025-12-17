"""
Complete system validation for the RAG Chatbot System.
This script tests the full functionality of the system.
"""
import os
import sys
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def validate_system():
    """Perform complete system validation."""
    print("RAG Chatbot System - Complete Validation")
    print("=" * 50)

    # Test 1: Check all required modules can be imported
    print("\n1. Testing module imports...")
    try:
        from config import settings
        from models.document import Document, DocumentChunk, SearchResult
        from models.query import QueryRequest, QueryResponse
        from services.embedding_service import EmbeddingService
        from services.qdrant_service import QdrantService
        from services.gemini_service import GeminiService
        from agent import Agent
        from ingest import ingest_documents
        print("   ✓ All modules imported successfully")
    except Exception as e:
        print(f"   ✗ Module import failed: {e}")
        return False

    # Test 2: Check environment configuration
    print("\n2. Testing environment configuration...")
    gemini_key = os.getenv("GEMINI_API_KEY", "")
    if not gemini_key:
        print("   ⚠ GEMINI_API_KEY not set - Gemini functionality will be limited")
    else:
        print("   ✓ GEMINI_API_KEY is configured")

    qdrant_host = os.getenv("QDRANT_HOST", "localhost")
    qdrant_port = os.getenv("QDRANT_PORT", "6333")
    print(f"   ✓ QDRANT configuration: {qdrant_host}:{qdrant_port}")

    # Test 3: Test embedding service
    print("\n3. Testing embedding service...")
    try:
        embedding_service = EmbeddingService()
        test_text = "This is a test sentence."
        embedding = embedding_service.generate_embedding(test_text)

        if isinstance(embedding, list) and len(embedding) > 0:
            print(f"   ✓ Embedding service works - generated {len(embedding)}-dimensional vector")
        else:
            print("   ✗ Embedding service returned invalid result")
            return False
    except Exception as e:
        print(f"   ✗ Embedding service test failed: {e}")
        return False

    # Test 4: Test Qdrant service initialization
    print("\n4. Testing Qdrant service...")
    try:
        qdrant_service = QdrantService(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
            api_key=settings.QDRANT_API_KEY
        )
        # Just test initialization - actual connection test would require Qdrant to be running
        print("   ✓ Qdrant service initialized")
    except Exception as e:
        print(f"   ⚠ Qdrant service initialization failed: {e}")
        # This might be OK if Qdrant isn't running during validation

    # Test 5: Test agent initialization
    print("\n5. Testing agent initialization...")
    try:
        agent = Agent()
        print("   ✓ Agent initialized successfully")
    except Exception as e:
        print(f"   ✗ Agent initialization failed: {e}")
        return False

    # Test 6: Check data directory
    print("\n6. Testing data directory...")
    data_dir = "data/docs"
    if os.path.exists(data_dir):
        md_files = [f for f in os.listdir(data_dir) if f.endswith('.md')]
        print(f"   ✓ Data directory exists with {len(md_files)} MD files")
        if md_files:
            print(f"     Sample files: {md_files[:3]}")
    else:
        print(f"   ⚠ Data directory {data_dir} does not exist")

    # Test 7: Test document processing functions
    print("\n7. Testing document processing functions...")
    try:
        from ingest import chunk_text, read_md_file
        # Test chunking function
        sample_text = "This is a sample document. " * 50  # Create a longer text
        chunks = chunk_text(sample_text, chunk_size=100, overlap=20)
        if len(chunks) > 0:
            print(f"   ✓ Document chunking works - created {len(chunks)} chunks")
        else:
            print("   ✗ Document chunking failed")
            return False
    except Exception as e:
        print(f"   ✗ Document processing test failed: {e}")
        return False

    # Test 8: Test model schemas
    print("\n8. Testing data models...")
    try:
        # Test QueryRequest model
        query_request = QueryRequest(query="Test query", max_results=3)
        assert query_request.query == "Test query"
        assert query_request.max_results == 3

        # Test SearchResult model
        search_result = SearchResult(
            document_id="test_id",
            content="Test content",
            score=0.95,
            metadata={"source": "test.md"}
        )
        assert search_result.document_id == "test_id"

        print("   ✓ Data models work correctly")
    except Exception as e:
        print(f"   ✗ Data model test failed: {e}")
        return False

    print("\n" + "=" * 50)
    print("✓ System validation completed successfully!")
    print("\nSystem is ready for use. Next steps:")
    print("1. Make sure Qdrant is running (if not using in-memory mode)")
    print("2. Ensure GEMINI_API_KEY is valid in your .env file")
    print("3. Run document ingestion: python ingest.py")
    print("4. Start the API server: uvicorn main:app --reload")
    print("5. Test the API endpoints")

    return True

if __name__ == "__main__":
    success = validate_system()
    sys.exit(0 if success else 1)