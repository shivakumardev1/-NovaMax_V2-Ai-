from pathlib import Path
import wave
import numpy as np
import sounddevice as sd

try:
    from resemblyzer import VoiceEncoder, preprocess_wav
except Exception:
    VoiceEncoder = None
    preprocess_wav = None

PROFILE = Path("data/owner_voice.npy")

def _record(seconds):
    sr = 16000
    audio = sd.rec(int(seconds * sr), samplerate=sr, channels=1, dtype="float32")
    sd.wait()
    return audio.reshape(-1), sr

def _save_wav(audio, sr, path):
    pcm = np.int16(np.clip(audio, -1, 1) * 32767)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(pcm.tobytes())

def enroll():
    if VoiceEncoder is None:
        raise RuntimeError("Install resemblyzer first.")
    PROFILE.parent.mkdir(exist_ok=True)
    print("6 seconds tak naturally bolo...")
    audio, sr = _record(6)
    temp = Path("data/_enroll.wav")
    _save_wav(audio, sr, temp)

    encoder = VoiceEncoder()
    embedding = encoder.embed_utterance(preprocess_wav(str(temp)))
    np.save(PROFILE, embedding)
    temp.unlink(missing_ok=True)
    print("Owner voice profile saved.")

def verify(seconds=4, threshold=0.70):
    # If the optional voice model isn't enrolled, return False rather than
    # silently pretending authentication succeeded.
    if VoiceEncoder is None or not PROFILE.exists():
        return False

    audio, sr = _record(seconds)
    temp = Path("data/_verify.wav")
    _save_wav(audio, sr, temp)

    encoder = VoiceEncoder()
    current = encoder.embed_utterance(preprocess_wav(str(temp)))
    owner = np.load(PROFILE)
    temp.unlink(missing_ok=True)

    score = float(
        np.dot(current, owner) /
        (np.linalg.norm(current) * np.linalg.norm(owner))
    )
    print("Voice similarity:", round(score, 3))
    return score >= threshold
