from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

from utils.speech_to_text import convert_audio_to_text
from utils.call_llm import get_llm_response
from utils.text_to_speech import convert_text_to_audio

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static', exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/ask', methods=['POST'])
def ask():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(audio_path)
        user_text = convert_audio_to_text(audio_path)
    else:
        user_text = request.json.get('text', '')

    response = get_llm_response(user_text)
    audio_url = convert_text_to_audio(response)

    return jsonify({
        "transcript": user_text,
        "reply": response,
        "audio_url": f"/{audio_url}" if audio_url else None
    })

@app.route('/static/<filename>')
def serve_audio(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
