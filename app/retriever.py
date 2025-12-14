from config.chroma_client import get_chroma_client
from services.embeddings import embed_sections
from config.llm_client import get_llm_client
from langchain.messages import SystemMessage,HumanMessage

def GetAnswer(query: str) -> str:
    try:
        client = get_chroma_client()
        collection = client.get_collection(name="University_IOOP_Sections")
    except Exception:
        return "Error connecting to ChromaDB"

    try:
        model = get_llm_client()
        embedding = embed_sections([query])
    except Exception:
        return "Error initializing model or embeddings"

    try:
        results = collection.query(query_embeddings=embedding, n_results=4)
    except Exception:
        return "Error querying ChromaDB"

    try:
        messages = [
            SystemMessage(
                content=f"Answer only from this text: {results}"
            ),
            HumanMessage(query)
        ]
        response = model.invoke(messages)
        return response.content or "No answer generated"
    except Exception:
        return "Error generating LLM response"
    

# print(GetAnswer("What is the Migration Fee"));




