<!-- Sync Impact Report:
Version change: 2.0.0 → 2.0.1
List of modified principles: Added Non-Negotiable Rules section with specific requirements
Added sections: Non-Negotiable Rules (API key hardcoding prohibition, Gemini context requirement, .env mandate, agent.py as central brain)
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/templates/commands/sp.constitution.md ⚠ pending
  - .specify/templates/commands/sp.phr.md ⚠ pending
  - .specify/templates/commands/sp.specify.md ⚠ pending
  - .specify/templates/commands/sp.plan.md ⚠ pending
  - .specify/templates/commands/sp.tasks.md ⚠ pending
  - .specify/templates/commands/sp.adr.md ⚠ pending
  - .specify/templates/commands/sp.implement.md ⚠ pending
  - .specify/templates/commands/sp.clarify.md ⚠ pending
  - .specify/templates/commands/sp.checklist.md ⚠ pending
  - .specify/templates/commands/sp.analyze.md ⚠ pending
  - .specify/templates/commands/sp.git.commit_pr.md ⚠ pending
Follow-up TODOs: None
-->
# RAG Chatbot System Constitution

## Core Principles

### I. Security First
All API keys and sensitive configurations must be managed through environment variables, never hardcoded. (.env file mandatory)

### II. Data Integrity
The system must only respond based on information retrieved from the ingested documentation, ensuring factual accuracy. (Gemini context required for all answers)

### III. Reproducible Workflow
The system must follow a clean, repeatable process for ingesting MD files, converting to vectors, and storing in Qdrant.

### IV. Proper Configuration
All components must be properly configured before operation, with clear error handling for misconfigurations. (agent.py as central brain)

## Non-Negotiable Rules

- ❌ API keys must never be hardcoded (enforced via .env file)
- ❌ System must not generate answers without proper Gemini context
- ✅ .env file usage is mandatory for all configurations
- ✅ agent.py serves as the central brain of the system

## Standards

- Documentation: MD files stored in my-website/docs
- Vector Storage: Qdrant for efficient similarity search
- AI Processing: Google Gemini for answer generation
- Security: Environment variables for all API keys and configs
- Code Quality: Clean, maintainable, well-documented code
- Error Handling: Comprehensive error reporting and graceful degradation

## Constraints

- Architecture: Backend system with secure API endpoints
- Dependency Management: Proper package management and version control
- Deployment: Container-ready with environment-based configuration
- Scalability: Designed to handle growing documentation sets
- Performance: Efficient document retrieval and response generation

## Governance

All changes to the RAG chatbot system must adhere to the following success criteria:
- No hardcoded secrets or API keys
- Proper integration with Qdrant vector database
- Accurate responses sourced only from documentation
- Secure configuration management
- Repeatable deployment process

**Version**: 2.0.1 | **Ratified**: 2025-12-16 | **Last Amended**: 2025-12-16