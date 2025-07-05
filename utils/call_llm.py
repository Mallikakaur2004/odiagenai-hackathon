import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "sarvamai/sarvam-m:free"

def extract_odia_only(text):
    return ''.join(re.findall(r'[ଁ-୷\s।]+', text)).strip()

def get_llm_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "Respond only in Odia script. No English. No reasoning. Only short, polite Odia answers."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        full_output = response.json()['choices'][0]['message']['content']
        return extract_odia_only(full_output)
    except Exception as e:
        print("[LLM Error]", e)
        return "[LLM Error] " + str(e)
