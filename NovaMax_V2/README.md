# NovaMax V2

Python voice-first desktop assistant.

## Setup — Windows

### 1. Python
Python 3.11/3.12 recommended.

### 2. Virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again.

### 3. Install packages

```powershell
pip install -r requirements.txt
```

If PyAudio fails, install a matching PyAudio wheel or use a Python version with a supported wheel.

### 4. Configure

Copy `.env.example` to `.env`.

### 5. Owner voice enrollment

```powershell
python enroll.py
```

Speak naturally for six seconds.

### 6. Optional local AI

Install Ollama separately and pull a model, for example:

```powershell
ollama pull llama3.2
```

Make sure Ollama is running.

### 7. Start Nova

```powershell
python main.py
```

Say:

- `Nova, VS Code kholo`
- `Nova, YouTube kholo`
- `Nova, Google par Python seekhne ke resources search karo`
- `Nova, mere liye portfolio website banao`
- `Nova, WhatsApp par Rahul ko message bhejna hai`
- `Nova, laptop lock karo`

## Security

Voice verification is a useful access layer, not a cryptographic guarantee. Keep Windows login/PIN enabled.

External communication uses confirmation and does not bypass WhatsApp authentication.

The assistant intentionally does not implement malware, credential theft, stealth persistence, security bypasses, or destructive arbitrary shell execution.
