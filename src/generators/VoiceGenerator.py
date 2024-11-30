from elevenlabs import ElevenLabs
import re

class AudioGenerator:
    def __init__(self, api_key: str, voice: str = "Adam", model: str = "eleven_multilingual_v2"):
        self.client = ElevenLabs(api_key=api_key)
        self.voice = voice
        self.model = model

    def _generate_audio(self, text: str, filename: str):
        audio = self.client.generate(
            text=text,
            voice=self.voice,
            model=self.model
        )
        audio_data = b''.join(audio)
        with open(filename, "wb") as f:
            f.write(audio_data)

    def generate_audio_from_texts(self, title: str, description: str):
        audio_title = self.format_audio_title(title)
        title_filename = f"{audio_title}.mp3"
        print(f"Gerando áudio para o título: {title}")
        self._generate_audio(title, title_filename)

        max_length = 500 
        parts = [description[i:i + max_length] for i in range(0, len(description), max_length)]

        for idx, part in enumerate(parts):
            description_filename = f"description_part_{idx + 1}.mp3"
            print(f"Gerando áudio para a parte {idx + 1} da descrição...")
            self._generate_audio(part, description_filename)

        print("Áudios gerados com sucesso!")
        
    def format_audio_title(self, text: str) -> str:
        text = text.lower()
        
        text = text.replace(" ", "_")
        
        text = re.sub(r"[^\w_]", "", text)
        return text