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

 ---

 If you'd like, I can:
 - Add a small architecture diagram for the README
 - Generate a `requirements.txt` or `pyproject.toml` if missing
 - Add example curl or Postman examples for the API

 Tell me which of these you'd like next.
Sure! Based on your project setup, here’s a **clean, professional, and complete `README.md`** ready for your LGU RAG system:

---

```markdown
# LGU RAG System (Retrieval-Augmented Generation)

A **RAG system** for Lahore Garrison University (LGU) that provides precise answers to student queries using ~100 pages of university content.  
The system leverages **LangChain**, **ChromaDB**, a **local embedding model** (`sentence-transformers/all-mpnet-base-v2`), and **Gemini 2.5 Flash Lite LLM**.

---

## Features

- Retrieve answers from university content using **semantic search**.  
- Local embeddings allow **offline query processing**.  
- RAG workflow: **Query → Embedding → ChromaDB retrieval → LLM answer**.  
- Handles questions on attendance, fees, exams, CGPA, courses, library rules, migration, and more.  
- Web-based interface with **dynamic input and instant responses**.  

---

## Tech Stack

- **Backend**: FastAPI + LangChain  
- **Vector Database**: ChromaDB  
- **Embeddings**: `sentence-transformers/all-mpnet-base-v2`  
- **LLM**: Gemini 2.5 Flash Lite  
- **Frontend**: HTML + JavaScript (dynamic DOM)  
- **Server**: Uvicorn  

---

## Project Structure

```

RUUUUG/
├── app/
│   ├── config/          # ChromaDB & LLM clients, settings
│   ├── services/        # Embeddings, PDF loader, Chroma store
│   ├── main.py          # FastAPI app
│   ├── retriever.py     # RAG logic (GetAnswer)
│   └── server.py        # Optional uvicorn launcher
├── index.html           # Frontend
├── ioop.pdf             # University content
├── README.md
├── .env
├── .gitignore
└── venv/

````

---

## Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/lgu-rag.git
cd lgu-rag
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

* Server runs at: `http://127.0.0.1:8000`

---

## API Endpoint

### `POST /query`

* **Request Body** (JSON):

```json
{
  "query": "What is the minimum attendance required for exams?"
}
```

* **Response** (JSON):

```json
{
  "answer": "The minimum attendance required to appear in final examinations is 75%."
}
```

---

## Frontend Usage

1. Open `index.html` in a browser.
2. Type your query in the input box.
3. Click **Retrieve**.
4. The answer from the RAG system will appear dynamically below the input.

**Note:** The frontend uses JavaScript `fetch()` to call the `/query` endpoint.

---

## CORS Configuration

To allow the frontend to access the backend, CORS is enabled in FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```

---

## Example Queries

* What is the minimum attendance percentage required to appear in final examinations?
* How much is the bank draft amount for BS self-finance admission?
* What is the duration of the End Semester Examination?
* Can students freeze more than two consecutive regular semesters?
* How many credit hours are required for MS/MPhil programs?

*(Supports 100+ FAQs from LGU content)*

---

## Troubleshooting

* **HTTP 500 errors** → Check server logs for LLM or ChromaDB errors.
* **Slow responses (~5s)** → LLM inference and embedding generation may take time; caching or async calls can help.
* **CORS issues** → Ensure `allow_origins` includes your frontend URL.

---

## License

MIT License © 2025

```

---

This README is:

- **Concise** and **to the point**  
- Includes **setup, usage, and API info**  
- Shows **project structure and example queries**  
- Covers **CORS and troubleshooting tips**

---

I can also generate a **visual diagram for the RAG workflow** (Query → Embedding → ChromaDB → LLM → Answer) to include in the README if you want it to be more visual and professional.  

Do you want me to add that?
```
