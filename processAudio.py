####### Work in progress to process the audio:
# 2 - If: the file is not .wav -> Convert to .wav -> 3
# 3 - If: Check for meta or multi channel
# 4 -   True: Remove meta or handle multi channel -> 5
# 5 -   False: Display time value of .wav in seconds

from pydub import AudioSegment
import wave

class AudioProcessor:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.audio = None
        self.metadata = False
        self.channels = 0

    def load_audio(self):
        self.audio = AudioSegment.from_file(self.audio_file)

    def check_properties(self):
        # Check for metadata
        self.metadata = len(self.audio.raw_data) > 0

        # Check the number of channels
        with wave.open(self.audio_file, 'rb') as wave_file:
            self.channels = wave_file.getnchannels()

    def convert_to_wav(self, output_wav_file):
        # Export the audio to WAV format
        self.audio.export(output_wav_file, format="wav")

    def process_wav(self, output_wav_file):
        # Remove metadata
        audio_without_metadata = self.audio.without_meta_data()

        # Handle multi-channel
        if self.channels > 1:
            # If more than one channel, split to mono
            audio_mono = audio_without_metadata.split_to_mono()
            processed_audio = audio_mono[0]  # Select the first channel (you may adjust based on your needs)
        else:
            processed_audio = audio_without_metadata

        # Export the processed audio to a new WAV file
        processed_audio.export(output_wav_file, format="wav")

# Example usage
if __name__ == "__main__":
    input_audio_file = "input.mp3"
    output_wav_file = "output.wav"

    audio_processor = AudioProcessor(input_audio_file)

    # Load and check properties
    audio_processor.load_audio()
    audio_processor.check_properties()

    print("Metadata:", audio_processor.metadata)
    print("Number of Channels:", audio_processor.channels)

    # Convert to WAV
    audio_processor.convert_to_wav(output_wav_file)

    # Process the WAV file
    audio_processor.process_wav(output_wav_file)
