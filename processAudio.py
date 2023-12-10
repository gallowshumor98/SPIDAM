# processAudio.py
from pydub import AudioSegment
import os

class AudioProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert_to_wav(self):
        # Load the audio file
        audio = AudioSegment.from_file(self.input_file)

        # Export the audio to WAV format
        audio.export(self.output_file, format="wav")
        print(f"Converted {self.input_file} to {self.output_file}")