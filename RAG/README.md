# Corrective RAG Implementation

## Overview

This project implements a Corrective Retrieval-Augmented Generation (RAG) system using LangGraph. The system intelligently decides whether a user query can be answered using a curated set of internal documents (OPM Annual Performance Reports from 2019–2022) or whether it should fall back to a live web search.

The workflow improves answer quality and reliability by:

1. Preferring trusted internal documents when sufficient information is available
2. Automatically routing to web search when document context is insufficient
3. Producing source-cited answers for transparency
4. The application is wrapped with a Gradio-based chat interface, making it easy to interact with and demo.

## Key Features
```
Corrective RAG Routing
Uses an LLM-based grading step to decide whether retrieved documents are sufficient to answer the question.

Document-Based Question Answering
Answers questions strictly from OPM annual performance documents (2019–2022) when relevant.

Web Search Fallback
Automatically performs a Tavily-powered web search if internal documents lack sufficient information.

Persistent Vector Store
Uses ChromaDB with OpenAI embeddings to persist document embeddings across runs.

Structured LLM Outputs
Ensures reliable routing and answer generation using Pydantic-based structured responses.

Interactive Chat UI
Gradio-based conversational interface with example queries for easy testing.
```

## Project Architecture Overview
```
├── RAG DataSet/
│ ├── 2019-annual-performance-report.pdf
│ ├── 2020-annual-performance-report.pdf
│ ├── 2021-annual-performance-report.pdf
│ └── 2022-annual-performance-report.pdf
│
├── chroma_db/
│ └── (Persistent Chroma vector store files)
│
├── perplexia_ai/
│ ├── core/
│ │ └── chat_interface.py # Base chat interface abstraction
│ │
│ └── RAGSearch/
│ └── Search/
│ ├── corrective_rag.py # Corrective RAG LangGraph workflow
│ ├── factory.py # Factory for RAG mode selection
│ └── prompts.py # All LLM prompts and schemas
│
├── app.py 
│ └── Gradio UI setup and launch
│
├── .env
│ └── API keys (OpenAI, Tavily)

```

## Technologies Used
```
Python 3.8+
LangChain 
LangGraph 
OpenAI GPT Models 
OpenAI Embeddings (text-embedding-3-small)
```

## Setup
```bash
Clone the Repository:
git clone https://github.com/ChakkaV1/RAG.git
cd RAG

Create a Virtual Environment:
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

Install Dependencies as per the technologies I used

API Keys & Environment Variables:
Create a .env file in the project root:
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key

Start the Gradio App:
python -m perplexia_ai.app

Access the Application:
Open your browser and go to http://127.0.0.1:7860
