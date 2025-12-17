"""
Startup test to ensure all RAG Chatbot System components are properly integrated.
"""
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_imports():
    """Check that all modules can be imported without errors."""
    print("Checking module imports...")

    modules_to_test = [
        ("config", "from config import settings"),
        ("models.document", "from models.document import Document, DocumentChunk, SearchResult"),
        ("models.query", "from models.query import QueryRequest, QueryResponse, HealthCheckResponse"),
        ("services.embedding_service", "from services.embedding_service import EmbeddingService"),
        ("services.qdrant_service", "from services.qdrant_service import QdrantService"),
        ("services.gemini_service", "from services.gemini_service import GeminiService"),
        ("agent", "from agent import agent, get_agent"),
        ("ingest", "from ingest import ingest_documents"),
    ]

    all_passed = True
    for module_name, import_statement in modules_to_test:
        try:
            exec(import_statement)
            print(f"✓ {module_name} - import successful")
        except ImportError as e:
            print(f"✗ {module_name} - import failed: {e}")
            all_passed = False
        except Exception as e:
            print(f"✗ {module_name} - error: {e}")
            all_passed = False

    return all_passed

def check_environment():
    """Check that required environment variables are set."""
    print("\nChecking environment configuration...")

    required_vars = ['GEMINI_API_KEY']
    optional_vars = ['QDRANT_HOST', 'QDRANT_PORT', 'QDRANT_API_KEY']

    all_set = True

    for var in required_vars:
        value = os.getenv(var)
        if not value:
            print(f"✗ {var} is not set (required)")
            all_set = False
        else:
            print(f"✓ {var} is set (required)")

    for var in optional_vars:
        value = os.getenv(var)
        if value:
            print(f"✓ {var} is set (optional: {value})")
        else:
            print(f"ℹ {var} is not set (optional, using default)")

    return all_set

def check_data_directory():
    """Check that the data directory exists and has files."""
    print("\nChecking data directory...")

    data_dir = "data/docs"
    if os.path.exists(data_dir):
        files = [f for f in os.listdir(data_dir) if f.endswith('.md')]
        print(f"✓ Data directory exists with {len(files)} MD files")
        if files:
            print(f"  Sample files: {files[:3]}")  # Show first 3 files
        return True
    else:
        print(f"✗ Data directory {data_dir} does not exist")
        return False

def main():
    """Run all startup checks."""
    print("RAG Chatbot System - Startup Integration Test")
    print("=" * 55)

    results = []

    results.append(("Imports", check_imports()))
    results.append(("Environment", check_environment()))
    results.append(("Data Directory", check_data_directory()))

    print("\n" + "=" * 55)
    print("Integration Test Summary:")

    all_passed = True
    for test_name, passed in results:
        status = "PASS" if passed else "FAIL"
        icon = "✓" if passed else "✗"
        print(f"{icon} {test_name}: {status}")
        if not passed:
            all_passed = False

    print()
    if all_passed:
        print("✓ All integration checks passed!")
        print("The RAG Chatbot System is properly integrated and ready for use.")
        print("\nNext steps:")
        print("1. Ensure Qdrant database is running")
        print("2. Verify your GEMINI_API_KEY is valid")
        print("3. Run document ingestion: python ingest.py")
        print("4. Start the API: uvicorn main:app --reload")
    else:
        print("✗ Some integration checks failed.")
        print("Please resolve the issues above before running the system.")

    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)