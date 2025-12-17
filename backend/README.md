# RAG Chatbot System

A Retrieval-Augmented Generation (RAG) chatbot system that ingests MD documentation files, stores them in Qdrant vector database, and uses Gemini LLM to generate contextually accurate responses based solely on the ingested documentation.

## Features

- Ingests MD documentation files automatically
- Stores document vectors in Qdrant for efficient similarity search
- Uses Google Gemini for response generation based on document context
- FastAPI-based API for querying the system
- Environment-based configuration for security

## Prerequisites

- Python 3.8+
- Qdrant vector database (can run locally or in cloud)
- Google Gemini API key

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment file and update with your values:

```bash
cp .env.example .env
```

Edit `.env` and set:
- `GEMINI_API_KEY`: Your Google Gemini API key
- `QDRANT_HOST`: Qdrant server host (default: localhost)
- `QDRANT_PORT`: Qdrant server port (default: 6333)

### 4. Prepare Documentation

Place your MD files in the `data/docs/` directory or copy them from your source location.

### 5. Run Document Ingestion

```bash
python ingest.py
```

This will chunk the MD files and store their vector representations in Qdrant.

## Usage

### 1. Start the API Server

```bash
python main.py
```

Or with uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Query the System

Once the server is running, you can send queries to the API:

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Your question here",
    "max_results": 5
  }'
```

### 3. Ingest New Documents

To ingest new documents after the server is running:

```bash
curl -X POST "http://localhost:8000/ingest"
```

## API Endpoints

- `GET /` - Health check
- `GET /health` - Detailed health check
- `POST /query` - Query the RAG system
- `POST /ingest` - Trigger document ingestion

## Architecture

The system follows a clean architecture with distinct responsibilities:

- `main.py`: FastAPI application (route handling only)
- `agent.py`: Central brain (query processing, context selection, response generation)
- `ingest.py`: Document ingestion pipeline
- `services/`: Individual service implementations (Qdrant, Gemini, Embedding)
- `models/`: Data models and schemas
- `config.py`: Configuration management

## Security

- All API keys are managed through environment variables
- No hardcoded credentials
- Proper validation and error handling

## Testing

### Validation Scripts

The system includes validation scripts to ensure proper setup:

```bash
# Run the system validation test
python test_rag_system.py

# Run the startup integration test
python startup_test.py
```

### Manual Testing

To run a quick manual test:

1. Start the server
2. Ingest some documents
3. Send a query to `/query` endpoint
4. Verify the response is generated from document context