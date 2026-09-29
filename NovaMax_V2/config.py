import os
from dotenv import load_dotenv

load_dotenv()

OWNER_NAME = os.getenv("OWNER_NAME", "Shiva")
WAKE_WORD = os.getenv("WAKE_WORD", "nova").lower()
VOICE_THRESHOLD = float(os.getenv("VOICE_THRESHOLD", "0.70"))
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
