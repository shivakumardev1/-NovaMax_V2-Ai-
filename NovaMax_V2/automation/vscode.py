import subprocess
from pathlib import Path

def open_vscode(path=None):
    target = str(Path(path).expanduser()) if path else str(Path.home())
    subprocess.Popen(["code", target], shell=True)
