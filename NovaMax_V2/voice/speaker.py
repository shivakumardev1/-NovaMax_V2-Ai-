import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

print("Available voices:")

for i, voice in enumerate(voices):
    print(i, voice.name)

if voices:
    engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)


def speak(text: str):
    print(f"Nova: {text}")

    try:
        engine.stop()
        engine.say(str(text))
        engine.runAndWait()

    except Exception as e:
        print(f"❌ TTS ERROR: {e}")