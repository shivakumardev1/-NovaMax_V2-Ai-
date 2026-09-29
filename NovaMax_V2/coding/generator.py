from pathlib import Path
import json
from core.brain import ask

BASE = Path.home() / "NovaMaxProjects"

def create_website(description):
    BASE.mkdir(exist_ok=True)
    project = BASE / "voice-website"
    project.mkdir(parents=True, exist_ok=True)

    prompt = f'''Create a frontend website for this request:
{description}

Return ONLY valid JSON with exactly these keys:
html, css, js

The HTML must reference style.css and script.js.
No markdown fences.'''

    raw = ask(prompt)

    try:
        data = json.loads(raw)
        html, css, js = data["html"], data["css"], data["js"]
    except Exception:
        return None, "AI ne valid website JSON return nahi kiya."

    (project / "index.html").write_text(html, encoding="utf-8")
    (project / "style.css").write_text(css, encoding="utf-8")
    (project / "script.js").write_text(js, encoding="utf-8")
    return project, "Website project ready hai."
