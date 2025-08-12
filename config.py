import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GPT_MODEL = "gpt-4o-mini"
TTS_MODEL = "gpt-4o-mini-tts"
DEFAULT_VOICE = "nova"
