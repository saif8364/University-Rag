 # LGU RAG System (Retrieval-Augmented Generation)

 A concise Retrieval-Augmented Generation (RAG) system that answers student queries using university documents.

 ## Overview

 This project embeds university content, stores vectors in Chroma, and uses an LLM to produce concise answers from retrieved passages. It is designed for local/experimental deployments and quick prototyping of RAG workflows.

 ## Key Features

 - Semantic retrieval from university documents
 - Local embeddings (sentence-transformers) and ChromaDB vector store
 - FastAPI backend with a simple HTML/JS frontend
 - Easy-to-run: `uvicorn` server for development

 ## Tech Stack

 - Backend: FastAPI
 - Vector DB: ChromaDB
 - Embeddings: sentence-transformers (e.g., `all-mpnet-base-v2`)
 - LLM: configured via `app/config/llm_client.py`
 - Server: Uvicorn

 ## Project Structure

 Top-level layout:

 RUUUUG/
 - app/
   - main.py        # FastAPI app entry
   - retriever.py   # RAG logic (embedding, retrieve, answer)
   - server.py      # Optional runner (uvicorn)
   - config/        # `chroma_client.py`, `llm_client.py`, `settings.py`
 - services/
   - chroma_store.py
   - embeddings.py
   - pdf_loader.py
 - index.html       # Simple web frontend
 - readme.md        # (this file)

 ## Quickstart (local)

 1. Create and activate a virtual environment:

 ```bash
 python -m venv venv
 venv\Scripts\activate    # Windows
 source venv/bin/activate  # macOS / Linux
 ```

 2. Install dependencies:

 ```bash
 pip install -r requirements.txt
 ```

 3. Run the server (development):

 ```bash
 cd app
 uvicorn server:app --reload
 ```

 Server default: `http://127.0.0.1:8000`

 ## API (example)

 POST `/query`

 Request JSON:

 ```json
 {
   "query": "What is the minimum attendance required for exams?"
 }
 ```

 Response JSON example:

 ```json
 {
   "answer": "The minimum attendance required to appear in final examinations is 75%.",
   "sources": ["ioop.pdf#page:12"]
 }
 ```

 Note: exact response fields depend on the implementation in `retriever.py`.

 ## Frontend

 - Open `index.html` in a browser (for local testing) or serve it via a static host.
 - The frontend uses `fetch()` to POST queries to the backend `/query` endpoint and displays the returned answer.

 ## Configuration

 - See `app/config/settings.py` for configurable parameters (Chroma path, embedding model, LLM options).
 - Keep secrets (API keys) out of the repo; use environment variables or a `.env` file.

 ## Development notes

 - To regenerate embeddings or repopulate Chroma, use the PDF loader in `services/pdf_loader.py` and the store logic in `services/chroma_store.py`.
 - For performance, consider caching embeddings and answers, and use async endpoints where appropriate.

 ## Troubleshooting

 - 500 errors: examine backend logs for LLM/Chroma exceptions.
 - CORS errors: set allowed origins in FastAPI CORS middleware.
 - Slow responses: embedding or LLM inference may be the bottleneck; measure and optimize.

 ## Contributing

 PRs welcome. For quick changes: fork → branch → PR. Describe changes and test locally.

 ## License

 MIT © 2025

 