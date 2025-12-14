from langchain.chat_models import init_chat_model
from config.settings import GEMINI_API_KEY
import os

# --- Validate the key ----
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# --- Set environment variable for LangChain ---
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# --- Initialize Gemini Model ---
def get_llm_client():
    model = init_chat_model("google_genai:gemini-2.5-flash-lite")
    return model
