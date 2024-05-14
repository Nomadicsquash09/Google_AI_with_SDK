import google.generativeai as genai
from pathlib import Path
import json
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
FILE_PATH = Path(__file__).parent
SETTINGS_PATH = FILE_PATH / 'settings.json'

with open(SETTINGS_PATH, 'r') as file:
    settings = json.load(file)

model = genai.GenerativeModel(
    model_name=settings["model_name"],
    generation_config=settings["generation_config"],
    safety_settings=settings["safety_settings"],
)

chat = model.start_chat(history=[])

while True:
    prompt = input("Pergunte: ")
    response = chat.send_message(prompt)
    print("\n", response.text)