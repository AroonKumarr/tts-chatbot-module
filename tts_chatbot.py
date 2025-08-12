import io
import wave
import simpleaudio as sa
from pydub import AudioSegment
from openai import OpenAI
import config

class TTSChatbot:
    def __init__(self, system_prompt="You are a helpful AI assistant."):
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        self.conversation_history = [{"role": "system", "content": system_prompt}]

    def chat(self, user_input: str) -> str:
        self.conversation_history.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model=config.GPT_MODEL,
            messages=self.conversation_history
        )

        reply = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": reply})
        return reply

    def speak(self, text: str, voice: str = config.DEFAULT_VOICE):
        audio_response = self.client.audio.speech.create(
            model=config.TTS_MODEL,
            voice=voice,
            input=text
        )

        audio_bytes = audio_response.content
        if not audio_bytes:
            print("⚠ No audio generated!")
            return

        audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")

        wav_io = io.BytesIO()
        audio_segment.export(wav_io, format="wav")
        wav_io.seek(0)

        with wave.open(wav_io, 'rb') as wave_read:
            wave_obj = sa.WaveObject(
                wave_read.readframes(wave_read.getnframes()),
                num_channels=wave_read.getnchannels(),
                bytes_per_sample=wave_read.getsampwidth(),
                sample_rate=wave_read.getframerate()
            )
            play_obj = wave_obj.play()
            play_obj.wait_done()

    def chat_and_speak(self, user_input: str):
        reply = self.chat(user_input)
        print("Bot:", reply)
        self.speak(reply)
        return reply


if __name__ == "__main__":
    bot = TTSChatbot()
    print("TTS Chatbot started! Type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                break
            bot.chat_and_speak(user_input)
        except Exception as e:
            print("⚠️ Error:", e)
