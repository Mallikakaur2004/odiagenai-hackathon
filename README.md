# SathiSwar 🎙️🇮🇳  
_A voice-first AI assistant empowering non-literate users across rural India to access vital government information—entirely through speech._

---

## 🧠 Problem Statement

In India, over 250 million people struggle with basic literacy, making it difficult to navigate digital systems like government portals, banking apps, or healthcare services. This digital divide especially impacts rural communities, elderly populations, and women with low exposure to tech platforms.

---

## 🔍 Solution Overview

**SathiSwar (ସାଥୀ ସ୍ୱର)** is a lightweight voice-based GenAI assistant that:

- Accepts spoken queries in Hindi, Odia, or other regional languages  
- Converts voice to text via Whisper or Vosk  
- Sends the transcription to GPT-style LLMs via OpenRouter  
- Converts the AI's response back to speech using Google TTS or Coqui  
- Replies to the user in their native language using audio—no screen or typing required

---

## 🧩 Tech Stack

| Layer              | Tool Used                    |
|-------------------|------------------------------|
| Speech-to-Text     | Whisper (OpenAI) / Vosk       |
| AI Reasoning       | OpenRouter (GPT-style models) |
| Text-to-Speech     | Google Cloud TTS / Coqui TTS  |
| Backend Server     | Python + Flask                |
| Frontend           | HTML + JavaScript / WhatsApp Bot |
| Hosting            | Replit / Render / GitHub Pages|

---

## 🛠️ Architecture Overview
```
[User Voice Input] 
        ↓ 
Speech Recognition (Whisper/Vosk)
        ↓ 
LLM via OpenRouter API 
        ↓ 
Text-to-Speech Conversion 
        ↓ 
[Voice Output in Regional Language]

```
---

## 🗺️ Use Case Demo

👩‍🌾 **User says:**  
> “Ration card kaise milega?”

🤖 **SathiSwar replies:**  
> “Aapko ration card ke liye gram panchayat mein form bharna hoga ya online bhi apply kar sakte hain…”

🎥 [Watch Demo Video](https://your-youtube-demo-link.com)

---

## 💡 Social Impact

**SathiSwar** bridges a digital accessibility gap by giving voice-based access to critical services for:
- Rural elders with little to no digital literacy  
- Women and first-time mobile users  
- Visually impaired or speech-limited users (coming soon)  
- Vernacular populations needing government/civic support

---

## 🧑‍🤝‍🧑 Team Members

- **Sibasish Mallick** – Voice Input Integration & Architecture, AI API Orchestration (OpenRouter)  
- **Mallika Kaur Kalha** – TTS Voice Design & Frontend Testing  
- **Khitish Routray** – UI/UX Workflow + Docs & Demo Recording

---


## 🚀 How to Run the Project
```
# 1. Clone the repo
git clone https://github.com/your-team/sathiswar.git
cd sathiswar

# 2. Set up dependencies
pip install -r requirements.txt

# 3. Add your API keys in `.env` file
# Example:
# OPENROUTER_API_KEY=your_openrouter_key
# GOOGLE_TTS_KEY=your_google_cloud_key

# 4. Run the app
python app.py

```

📘 Repo Contents
```
sathiswar/
├── app.py
├── requirements.txt
├── .env.example
├── /templates
│   └── index.html
├── /utils
│   ├── speech_to_text.py
│   ├── call_llm.py
│   └── text_to_speech.py
└── /test
    └── test_pipeline.py
```

“With SathiSwar, we’re not just building an app—we’re building an audible bridge to digital India.” 🇮🇳✨
