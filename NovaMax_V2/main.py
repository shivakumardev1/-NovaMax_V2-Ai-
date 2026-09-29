import re

from config import WAKE_WORD, VOICE_THRESHOLD
from voice.listener import listen
from voice.speaker import speak
from voice.authentication import verify
from core.brain import ask
from automation.windows import open_app, open_folder, lock_pc
from automation.browser import open_url, search
from automation.vscode import open_vscode
from coding.generator import create_website
from whatsapp.controller import prepare_whatsapp

def confirmation(question):
    speak(question + " Haan ya nahi?")
    answer = listen(timeout=6, phrase_limit=4)
    return "haan" in answer or "yes" in answer

def handle(command):
    if command in ("stop", "exit", "quit") or "band ho jao" in command:
        speak("Okay babu, standby par ja rahi hoon.")
        raise SystemExit

    if "vs code" in command and ("open" in command or "khol" in command):
        open_vscode()
        speak("VS Code khol diya.")
        return

    if "notepad" in command and ("open" in command or "khol" in command):
        open_app("notepad")
        speak("Notepad khol diya.")
        return

    if "calculator" in command and ("open" in command or "khol" in command):
        open_app("calculator")
        speak("Calculator khol diya.")
        return

    if "youtube" in command:
        open_url("https://www.youtube.com")
        speak("YouTube khol diya.")
        return

    if "google par" in command or "google pe" in command:
        q = re.sub(r".*google (?:par|pe)\s*", "", command).strip()
        if q:
            search(q)
            speak("Google par search kar diya.")
        return

    if ("website" in command or "web site" in command) and any(
        x in command for x in ("banao", "create", "make")
    ):
        speak("Website kis topic par banani hai?")
        idea = listen(timeout=10, phrase_limit=15)
        if not idea:
            speak("Idea clear nahi mila.")
            return

        speak("Website generate kar rahi hoon.")
        project, result = create_website(idea)
        if project:
            open_vscode(project)
        speak(result)
        return

    if "whatsapp" in command:
        speak("Kis contact ko message bhejna hai?")
        contact = listen(timeout=8, phrase_limit=8)
        if not contact:
            speak("Contact nahi mila.")
            return

        speak("Message bolo.")
        message = listen(timeout=10, phrase_limit=15)
        if not message:
            speak("Message nahi mila.")
            return

        if confirmation(f"{contact} ko WhatsApp par ye message prepare karun: {message}"):
            speak(prepare_whatsapp(contact, message))
        else:
            speak("Cancel kar diya.")
        return

    if "laptop lock" in command or "computer lock" in command:
        if confirmation("Laptop lock kar doon?"):
            lock_pc()
        return

    reply = ask(command)
    speak(reply)

def main():
    speak("NovaMax V2 online hai. Wake word Nova hai.")

    while True:
        try:
            heard = listen()
            if WAKE_WORD not in heard:
                continue

            # if not verify(threshold=VOICE_THRESHOLD):
            #     speak("Voice verification failed. Access denied.")
            #     continue

            speak("Haan babu, bolo.")
            command = listen(timeout=10, phrase_limit=20)

            if command:
                handle(command)

        except KeyboardInterrupt:
            print("\nNovaMax stopped.")
            break
        except SystemExit:
            break
        except Exception as exc:
            print("Error:", exc)
            speak("Ek technical error aa gayi.")

if __name__ == "__main__":
    main()
