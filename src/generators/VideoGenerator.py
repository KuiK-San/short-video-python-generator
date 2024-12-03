from moviepy import VideoFileClip, AudioFileClip

class VideoAudioMerger:
    def __init__(self, video_path: str, audio_path: str, output_path: str):
        """
        Inicializa os caminhos do vídeo, áudio e saída.
        """
        self.video_path = video_path
        self.audio_path = audio_path
        self.output_path = output_path
        self.video_clip = None
        self.audio_clip = None

    def load_clips(self):
        """
        Carrega o vídeo e o áudio.
        """
        try:
            self.video_clip = VideoFileClip(self.video_path)
            self.audio_clip = AudioFileClip(self.audio_path)
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivos: {e}")

    def merge(self):
        """
        Junta o áudio com o vídeo, ajustando a duração se necessário.
        """
        if not self.video_clip or not self.audio_clip:
            raise Exception("Os clipes de vídeo e áudio precisam ser carregados primeiro.")

        if self.audio_clip.duration < self.video_clip.duration:
            self.video_clip = self.video_clip.subclip(0, self.audio_clip.duration)

        self.video_clip = self.video_clip.set_audio(self.audio_clip)

    def save(self):
        """
        Salva o arquivo final no caminho de saída.
        """
        if not self.video_clip:
            raise Exception("O vídeo com áudio não foi gerado. Execute o método merge primeiro.")
        self.video_clip.write_videofile(self.output_path, codec="libx264", audio_codec="aac")
        print(f"Vídeo salvo em: {self.output_path}")
