import requests
from config import OLLAMA_URL, OLLAMA_MODEL

SYSTEM = '''You are NovaMax, a friendly female-style desktop AI assistant.
Speak naturally in Hindi/Hinglish when the user does.
Help with coding, productivity, files and normal conversation.
Never claim an action happened unless the controller confirms it.
Do not provide malware, credential theft, stealth persistence, destructive automation,
or ways to bypass authentication/security.'''

def ask(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM},
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    except Exception as exc:
        return f"Local AI available nahi hai. Ollama check karo: {exc}"
