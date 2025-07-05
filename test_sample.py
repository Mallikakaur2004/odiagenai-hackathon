from utils.speech_to_text import convert_audio_to_text
from utils.call_llm import get_llm_response
from utils.text_to_speech import convert_text_to_audio

AUDIO_PATH = "uploads/sample_odia.wav"

# Step 1: Transcribe
transcript = convert_audio_to_text(AUDIO_PATH)
print("🎙️ STT Output:", transcript)

# Step 2: Get LLM response
if transcript and not transcript.startswith("[STT Error]"):
    reply = get_llm_response(transcript)
    print("🤖 LLM Reply:", reply)
else:
    print("❌ Skipping LLM due to STT failure.")
    reply = ""

# Step 3: Convert to Audio (TTS)
if reply and not reply.startswith("[LLM Error]"):
    audio_path = convert_text_to_audio(reply)
    if audio_path:
        print("🔊 TTS Output File:", audio_path)
    else:
        print("❌ TTS failed — no audio generated.")
else:
    print("❌ Skipping TTS due to LLM failure.")
