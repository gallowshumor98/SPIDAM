########6 - Display the waveform from file - needs modified
import wave
import numpy as np
import matplotlib.pyplot as plt
# from scipy.io import wavfile

def plot_waveform(wave_file):
    # Open the wave file
    with wave.open(wave_file, 'rb') as wf:
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
        plt.title('Waveform of {}'.format(wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.show()

# Replace 'your_file.wav' with the path to your .wav file
plot_waveform('your_file.wav')