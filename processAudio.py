from pydub import AudioSegment
import os

class AudioProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def process(self):
        # Processes the audio and then converts the file to .wav format
        raw_audio = AudioSegment.from_file(self.input_file)
        channel_count = raw_audio.channels
        print("Original Channels:", channel_count)
        mono_audio = raw_audio.set_channels(1)
        channel_count_mono = mono_audio.channels
        print("Mono Channels:", channel_count_mono)
        mono_audio.export(self.output_file, format="wav")  