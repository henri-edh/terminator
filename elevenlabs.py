import requests  # Used for making HTTP requests
import os

CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
XI_API_KEY = os.environ.get('ELEVENLABS_API_KEY')
VOICE_ID = "1ea1QuvY41JPWJPfwbBJ"  # ID of the voice model to use
OUTPUT_PATH = "output.mp3"  # Path to save the output audio file

tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

headers = {
    "Accept": "application/json",
    "xi-api-key": XI_API_KEY
}

def speak(text):
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }

    response = requests.post(tts_url, headers=headers, json=data, stream=True)

    if response.ok:
        with open(OUTPUT_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        print("Audio stream saved successfully.")
    else:
        print(response.text)