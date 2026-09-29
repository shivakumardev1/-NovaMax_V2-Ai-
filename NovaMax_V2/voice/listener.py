import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5


def listen(timeout=8, phrase_limit=12):
    try:
        with sr.Microphone() as source:

            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            print("🎤 Speak now...")

            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_limit
            )

        print("🔄 Converting speech to text...")

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        text = text.lower().strip()

        print(f"👤 You: {text}")

        return text

    except sr.WaitTimeoutError:
        print("⚠️ Listening timeout: koi voice nahi mili.")
        return ""

    except sr.UnknownValueError:
        print("⚠️ Voice samajh nahi aayi.")
        return ""

    except sr.RequestError as e:
        print(f"❌ Google Speech Recognition error: {e}")
        return ""

    except Exception as e:
        print(f"❌ Microphone error: {e}")
        return ""