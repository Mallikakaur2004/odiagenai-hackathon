# SathiSwar 🎙️🇮🇳  
_A voice-first AI assistant empowering non-literate users across rural India to access vital government information—entirely through speech._

---

## 🧠 Problem Statement

In India, over 250 million people struggle with basic literacy, making it difficult to navigate digital systems like government portals, banking apps, or healthcare services. This digital divide especially impacts rural communities, elderly populations, and women with low exposure to tech platforms.

---

## 🔍 Solution Overview

**SathiSwar (ସାଥୀ ସ୍ୱର)** is a lightweight voice-based GenAI assistant that:

- Accepts spoken queries in Odia, Hindi, or other regional languages  
- Converts voice to text using **Sarvam.ai STT API**  
- Sends the transcription to powerful **GPT-style LLMs** via **OpenRouter**  
- Converts the AI's Odia text response back to speech via **Sarvam.ai TTS API**  
- Replies to the user in Odia using audio—no need for typing, reading, or screens  

> 🎯 The experience feels like talking to a helpful human assistant — in your own language.

---

## 🧩 Tech Stack

| Layer              | Tool Used                         |
|-------------------|-----------------------------------|
| Speech-to-Text     | Sarvam.ai (saarika:v2.5)           |
| AI Reasoning       | OpenRouter (e.g. sarvam-m LLM)     |
| Text-to-Speech     | Sarvam.ai (bulbul:v2)              |
| Backend Server     | Python + Flask                     |
| Frontend           | HTML, CSS, JavaScript (no canvas)  |
| Hosting (optional) | Render / Replit / Localhost        |

---

## 🛠️ Architecture Overview

```
  [🎙 User Voice Input]
          ↓
📥 Speech-to-Text (Sarvam.ai)
          ↓
🧠 LLM Processing (OpenRouter API)
          ↓
 📤 Text-to-Speech (Sarvam.ai)
          ↓
 [🔊 Voice Reply in Odia]
```


---

## 🗺️ Use Case Demo

👩‍🌾 **User says (in Odia):**  
> “ରାସନ୍ କାର୍ଡ କିପରି ମିଳିବ?”

🤖 **SathiSwar replies (in Odia):**  
> “ରାସନ୍ କାର୍ଡ ପାଇଁ ଆପଣ ଗ୍ରାମ ପଞ୍ଚାୟତ କିମ୍ବା ଓନଲାଇନରେ ଆବେଦନ କରିପାରିବେ…”

🎥 [Watch Demo Video](https://your-youtube-demo-link.com)

---

## 💡 Social Impact

**SathiSwar** bridges India’s digital accessibility gap by enabling:

- 📱 Rural elders with no digital literacy  
- 👩‍🦱 Women and first-time smartphone users  
- 👀 Visually impaired users (TTS-only mode coming soon)  
- 🗣️ Vernacular users needing civic/government support  

All without typing or reading — just through conversation in their own language.

---

## 🧑‍🤝‍🧑 Team Members

- **Sibasish Mallick** – Backend Architecture, Voice Input Integration, AI Orchestration (OpenRouter)  
- **Mallika Kaur Kalha** – Odia Voice Design, Frontend Integration, Usability Testing  
- **Khitish Routray** – UI/UX Design, Workflow Diagrams, Demo Recording & Documentation  

---

## 🚀 How to Run the Project

```bash
# 1. Clone the repo
git clone https://github.com/your-team/sathiswar.git
cd sathiswar

# 2. Set up virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install required Python packages
pip install -r requirements.txt

# 4. Add your API keys in `.env` file
# Example:
# OPENROUTER_API_KEY=your_openrouter_key
# SARVAM_API_KEY=your_sarvam_api_key

# 5. Run the app
python app.py
```

📘 Repo Structure
```
sathiswar/
├── app.py                       # Main Flask application
├── requirements.txt             # Python dependencies
├── .env.example                 # Example environment variables
│
├── /templates/
│   └── index.html               # Frontend HTML UI
│
├── /static/
│   ├── style.css                # Stylesheet for chat UI
│   ├── script.js                # JavaScript for mic and chat logic
│   └── images/                  # Logos, icons, and media
│
├── /utils/
│   ├── call_llm.py              # Connects to OpenRouter for LLM response
│   ├── speech_to_text.py        # Sarvam.ai STT transcription
│   └── text_to_speech.py        # Sarvam.ai TTS voice generation
│
├── /uploads/
│   └── sample_odia.wav          # Sample file for testing STT
│
└── /test/
    └── test_sample.py           # CLI test script for STT → LLM → TTS
```

🔒 Environment Configuration
```
OPENROUTER_API_KEY=your_openrouter_api_key
SARVAM_API_KEY=your_sarvam_ai_api_key

```

## Key Highlights
✅ Works completely via speech — ideal for illiterate users
✅ Designed with Indian regional languages in mind (currently focused on Odia)
✅ Lightweight architecture and no heavy dependencies
✅ Modular and testable backend with plug-and-play APIs
✅ Professional frontend UI with dark/light mode and speech bubbles

## Future Roadmap
🔁 Add multi-language auto-detection
📞 Deploy as a WhatsApp voice bot
📱 Package as an Android APK or PWA
🧑‍🦯 Enable screen reader compatibility and voice-only workflows
🌐 Add support for more civic/government services

🗣️ “With SathiSwar, we’re not just building an app—we’re building an audible bridge to digital India.” 🇮🇳✨

