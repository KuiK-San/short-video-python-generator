from moviepy.editor import VideoFileClip, AudioFileClip

class VideoAudioMerger:
    def __init__(self, video_path: str, audio_path: str, output_path: str):
        self.video_path = video_path
        self.audio_path = audio_path
        self.output_path = output_path
        self.video_clip = None
        self.audio_clip = None

    def load_clips(self):
        try:
            self.video_clip = VideoFileClip(self.video_path)
            self.audio_clip = AudioFileClip(self.audio_path)
            print(f"Vídeo e áudio carregados com sucesso.")
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivos: {e}")

    def merge(self):
        if not self.video_clip or not self.audio_clip:
            raise Exception("Os clipes de vídeo e áudio precisam ser carregados primeiro.")
        if self.audio_clip.duration < self.video_clip.duration:
            self.video_clip = self.video_clip.subclip(0, self.audio_clip.duration)
        self.video_clip = self.video_clip.set_audio(self.audio_clip)

    def add_subtitles(self, srt_path: str, font='Arial', fontsize=24, color='white'):
        return

    def save(self):
        if not self.video_clip:
            raise Exception("O vídeo com áudio não foi gerado. Execute o método merge primeiro.")
        self.video_clip.write_videofile(self.output_path, codec="libx264", audio_codec="aac")
        print(f"Vídeo salvo em: {self.output_path}")

# Exemplo de uso
if __name__ == "__main__":
    video_path = "./src/public/video_background.mp4"
    audio_path = "./audio_output.mp3"
    output_path = "video_com_audio_e_legendas.mp4"
    srt_path = "./legendas_auto.srt"

    merger = VideoAudioMerger(video_path, audio_path, output_path)
    
    try:
        merger.load_clips()
        merger.merge()
        merger.save()
    except Exception as e:
        print(f"Erro: {e}")
