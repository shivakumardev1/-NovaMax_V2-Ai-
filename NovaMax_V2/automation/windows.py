import subprocess
import os
from pathlib import Path

def open_app(name):
    apps = {
        "notepad": ["notepad.exe"],
        "calculator": ["calc.exe"],
        "paint": ["mspaint.exe"],
    }
    cmd = apps.get(name.lower())
    if not cmd:
        return False
    subprocess.Popen(cmd)
    return True

def open_folder(path):
    p = Path(path).expanduser()
    if not p.exists():
        return False
    os.startfile(str(p))
    return True

def lock_pc():
    # Safe Windows lock action.
    subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"], check=False)
