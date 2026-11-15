
# SkillBridge Student Academics Agent

## Project Overview

An Agentic RAG-based academic assistant for SkillBridge EdTech.

The application answers student questions using structured CSV datasets,
academic policy documents, Python calculation tools and a local LLM.

## Features

- Student information retrieval
- Course information retrieval
- Assessment lookup
- Attendance lookup
- Mentor information retrieval
- Academic policy retrieval
- FAISS vector database
- MMR-based document retrieval
- Ollama local LLM
- Python calculation tools
- Tool-calling agent loop
- Streamlit chatbot interface

## Technology Stack

- Python
- Ollama
- Qwen 2.5
- Nomic Embeddings
- LangChain
- FAISS
- Pandas
- Streamlit

## Project Structure

```text
Agentic_RAG_SkillBridge/
├── data/
├── policies/
├── vector_store/
├── src/
├── app.py
├── requirements.txt
├── test_agent.py
└── README.md
```

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies.
4. Install Ollama.
5. Download the required Ollama models.
6. Add permitted datasets and policy files.
7. Run the application.

## Run

```bash
streamlit run app.py
```

