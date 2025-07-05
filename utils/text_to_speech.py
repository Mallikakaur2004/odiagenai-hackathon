import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

def convert_text_to_audio(text, language_code="od-IN"):
    url = "https://api.sarvam.ai/text-to-speech"
    headers = {
        "API-Subscription-Key": SARVAM_API_KEY
    }
    data = {
        "text": text,
        "target_language_code": language_code,
        "model": "bulbul:v2",
        "speaker": "anushka"
    }
    try:
        resp = requests.post(url, headers=headers, json=data)
        resp.raise_for_status()
        audio_b64 = resp.json()["audios"][0]
        audio_bytes = base64.b64decode(audio_b64)
        output_path = f"static/response_{os.urandom(4).hex()}.wav"
        with open(output_path, "wb") as f:
            f.write(audio_bytes)
        return output_path
    except Exception as e:
        print("[TTS Error]", e)
        return None
