# RAG Chatbot System Specification

## Overview

A Retrieval-Augmented Generation (RAG) chatbot system that ingests MD documentation files, stores them in Qdrant vector database, and uses Gemini LLM to generate contextually accurate responses based solely on the ingested documentation.

## Tech Stack

- **Backend**: FastAPI
- **Agent**: Custom agent.py (central brain)
- **Vector Database**: Qdrant
- **LLM**: Google Gemini
- **Embeddings**: Qwen
- **Documentation Source**: MD files from my-website/docs
- **Workflow**: SpecifyPlus methodology

## Collections

### docs
- **Purpose**: Stores the original MD documentation files
- **Structure**: Contains raw MD content with metadata
- **Access**: Read-only for ingestion process

### selected_docs
- **Purpose**: Stores user-selected text segments relevant to queries
- **Structure**: Contains vector embeddings and associated text chunks
- **Access**: Used during query processing to find relevant context

## Core Rules

### Prohibited Actions
- ❌ No manual copy-paste operations (automated workflow only)
- ❌ No answers generated outside of provided context (strict RAG adherence)

### Required Behaviors
- ✅ Agent decides everything (agent.py as central decision-maker)
- ✅ FastAPI serves only as route handler (thin API layer)

## Functional Requirements

### 1. Document Ingestion
- System must automatically scan MD files in my-website/docs
- Convert MD content to vector embeddings using Qwen
- Store embeddings in Qdrant docs collection
- Preserve original document structure and metadata

### 2. Query Processing
- User submits query via FastAPI endpoint
- Agent.py processes query and searches relevant docs in Qdrant
- Relevant document segments stored in selected_docs collection
- Gemini generates response based on selected context

### 3. Response Generation
- Gemini only responds based on content from selected_docs
- No external knowledge or hallucination allowed
- Response must cite source documents when possible
- Error handling for insufficient context scenarios

## Non-Functional Requirements

### Security
- API keys stored in .env files (no hardcoding)
- All configurations managed through environment variables
- Secure endpoint authentication

### Performance
- FastAPI endpoints must respond within 5 seconds
- Qdrant vector searches under 1 second
- Gemini response generation under 3 seconds

### Reliability
- System must handle 100 concurrent users
- 99.9% uptime requirement
- Graceful degradation when Qdrant or Gemini unavailable

## Architecture Constraints

- FastAPI only handles HTTP routing, no business logic
- All decision-making happens in agent.py
- Direct Qdrant access only through agent.py
- No manual data manipulation in collections
- All embeddings generated via Qwen model

## Success Criteria

- ✅ System ingests MD files automatically
- ✅ Accurate responses based solely on documentation
- ✅ No hardcoded API keys or configs
- ✅ Agent.py controls all business logic
- ✅ FastAPI acts as pure route handler
- ✅ No manual copy-paste operations required
- ✅ All responses stay within context boundaries