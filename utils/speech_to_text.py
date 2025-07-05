import os
import requests
from dotenv import load_dotenv

load_dotenv()
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

def convert_audio_to_text(file_path):
    url = "https://api.sarvam.ai/speech-to-text"
    headers = {
        "api-subscription-key": SARVAM_API_KEY
    }
    with open(file_path, "rb") as audio_file:
        files = {
            "file": (os.path.basename(file_path), audio_file, "audio/wav")
        }
        data = {
            "language_code": "od-IN",
            "model": "saarika:v2.5"
        }
        try:
            resp = requests.post(url, headers=headers, files=files, data=data)
            resp.raise_for_status()
            transcript = resp.json().get("transcript", "")
            print("🎙️ Transcribed Odia Text:", transcript)
            return transcript
        except Exception as e:
            print("[STT Error]", e)
            return "[STT Error] " + str(e)
