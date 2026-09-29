from pathlib import Path
import json

FILE = Path("data/memory.json")

def load():
    FILE.parent.mkdir(exist_ok=True)
    if not FILE.exists():
        FILE.write_text("[]", encoding="utf-8")
    try:
        return json.loads(FILE.read_text(encoding="utf-8"))
    except Exception:
        return []

def add(note):
    data = load()
    data.append(note)
    FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
