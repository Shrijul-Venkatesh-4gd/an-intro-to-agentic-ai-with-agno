# An Introduction to Agentic AI with Agno

A hands-on course that introduces the core building blocks of agentic AI systems using the [Agno](https://github.com/agno-agi/agno) framework.

## What You Will Learn

The course is structured as a progression of concepts, each building on the last:

| # | Concept | What it covers |
|---|---------|----------------|
| 1 | **Echo Agent** | Your first agent — structured output and basic agent configuration |
| 2 | **Chatbot Agent** | Conversational memory using an in-memory session store |
| 3 | **RAG Agent** | Retrieval-Augmented Generation with a LanceDB vector store |
| 4 | **Teams** | Multi-agent coordination — a writer and reviewer working together |
| 5 | **Workflows** | Sequential pipelines — a researcher feeding into a writer |

## Project Structure

```
agents/       # Agent definitions (one per concept)
cookbook/     # Runnable scripts for each agent/concept
models/       # Pydantic output schemas
database/     # Vector store (LanceDB) and relational DB (Postgres) setup
utils/        # Shared settings and configuration
```

## Prerequisites

- Python 3.13+
- An [OpenRouter](https://openrouter.ai) API key

## Setup

```bash
# Install dependencies
pip install -e .

# Copy the example env file and add your API key
cp .env.example .env
```

## Running the Examples

Each concept has a corresponding script in `cookbook/`:

```bash
python cookbook/echo_run.py
python cookbook/chatbot_run.py
python cookbook/rag_run.py
python cookbook/team_run.py
python cookbook/workflow_run.py
```
