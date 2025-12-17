---
id: 0002
title: Update RAG Chatbot System Constitution
stage: constitution
date: 2025-12-16
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: MUBASHIR
command: /sp.constitution
labels: [constitution,rag,chatbot,security]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - ../.specify/memory/constitution.md
tests:
  - none
---

## Prompt

```
Problem

Docs MD files mein hain (my-website/docs)

Chatbot bina proper config ke kaam nahi kar raha

API keys hard-code karna unsafe hai

Workflow scattered hai

Goal

Backend mein ek secure, clean, repeatable RAG chatbot system banana jo:

MD docs ko ingest kare

Qdrant mein vectors store kare

Gemini se answers generate kare

Sirf docs se jawab de

Environment variables se securely run ho

SpecifyPlus ke steps strictly follow kare

Constitution updated to include Non-Negotiable Rules.
Non-Negotiable Rules

❌ API keys hard-code nahi hongi

❌ Gemini context ke baghair answer nahi dega

✅ .env file mandatory

✅ agent.py central brain hoga
```

## Response snapshot

Updated the project constitution to reflect requirements for a secure RAG chatbot system that:
- Uses environment variables for API keys (no hardcoded values) - .env file mandatory
- Ingests MD documentation files
- Stores vectors in Qdrant
- Generates answers with Google Gemini only when proper context is available
- Responds only based on documentation content
- Follows proper configuration management with agent.py as central brain

The constitution was updated from version 1.0.1 to 2.0.0 with new core principles focused on security, data integrity, reproducible workflow, and proper configuration. Then updated to 2.0.1 to include explicit Non-Negotiable Rules section.

## Outcome

- ✅ Impact: Constitution updated with explicit Non-Negotiable Rules for security and functionality
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated
- 🔁 Next prompts: Plan and implement the RAG chatbot system based on new constitution
- 🧠 Reflection: Version updated to 2.0.1 to reflect addition of critical non-negotiable rules

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): Begin implementation of RAG system according to new constitution