########6 - Display the waveform from file - needs modified
import wave
import numpy as np
import matplotlib.pyplot as plt
# from scipy.io import wavfile

class WaveformPlotter:
    def __init__(self, wave_file):
        self.wave_file = wave_file

    def plot_waveform(self):
        # Open the wave file
        with wave.open(self.wave_file, 'rb') as wf:
            # Get the parameters of the wave file
            params = wf.getparams()
            
            # Read the audio data
            audio_data = wf.readframes(params.nframes)
            
            # Convert the binary audio data to a NumPy array
            audio_array = np.frombuffer(audio_data, dtype=np.int16)
            
            # Create a time axis for the waveform
            time_axis = np.arange(0, params.nframes) / params.framerate
            
            # Plot the waveform
            plt.plot(time_axis, audio_array)
            plt.title('Waveform of {}'.format(self.wave_file))
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')
            plt.show()

# Example usage
#waveform_plotter = WaveformPlotter('PolyHallClap_10mM.WAV')
#waveform_plotter.plot_waveform()