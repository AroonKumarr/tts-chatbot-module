# TTS Chatbot Module

A Python module for a conversational AI chatbot with Text-to-Speech (TTS) capabilities using OpenAI API.

---

## Features

- Chat with an AI assistant powered by OpenAI GPT model.
- Generate speech audio responses with OpenAI TTS model.
- Play audio responses locally.
- Maintains conversation history. 

---

## Files

- `tts_chatbot.py` — Main chatbot class with chat and speak methods.
- `config.py` — Configuration file to load API keys and model settings.
- `requirements.txt` — Python dependencies required for this module.
- `.env` — Environment file to store your OpenAI API key securely.
- `__init__.py` — Makes this folder a Python package (optional).

---

## Setup

1. Clone or download this repository.

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Create a .env file in the root folder with your OpenAI API key:


OPENAI_API_KEY=your_openai_api_key_here
Usage
Import and create an instance of the chatbot:


from tts_module import TTSChatbot  # or your folder name

bot = TTSChatbot()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    bot.chat_and_speak(user_input)
Requirements
Python 3.8+

OpenAI API key with access to GPT and TTS models

Packages listed in requirements.txt

Notes
The module plays audio using simpleaudio and converts audio formats with pydub.

Make sure you have ffmpeg installed on your system for pydub to work with mp3 files.

Adjust model names in config.py as needed.

License
MIT License
