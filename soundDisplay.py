########6 - Display the waveform from file
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from scipy.io import wavfile

class WaveformPlotter:
    def __init__(self, wave_file):
        self.wave_file = wave_file
        self.audio_array = None
        self.time_axis = None

    def read_wave_file(self):
        # Open the wave file
        with wave.open(self.wave_file, 'rb') as wf:
            # Get the parameters of the wave file
            params = wf.getparams()

            # Read the audio data
            audio_data = wf.readframes(params.nframes)

            # Convert the binary audio data to a NumPy array
            self.audio_array = np.frombuffer(audio_data, dtype=np.int16)

            # Create a time axis for the waveform
            self.time_axis = np.arange(0, params.nframes) / params.framerate

    def plot_waveform(self):
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        
        plt.clf()
        # Plot the waveform
        plt.plot(self.time_axis, self.audio_array)
        plt.title('Waveform of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        
        # Perform frequency domain analysis using Fast Fourier Transform (FFT)
        spectrum = np.fft.fft(self.audio_array)
        frequencies = np.fft.fftfreq(len(spectrum), d=self.time_axis[1] - self.time_axis[0])

        # Find the index corresponding to the maximum amplitude (excluding DC component)
        max_index = np.argmax(np.abs(spectrum[1:])) + 1

        # Compute the corresponding frequency in Hz
        highest_resonance_freq = np.abs(frequencies[max_index])
        
        # Display highest frequency as text annotation
        plt.annotate('Highest Resonance: {:.2f} Hz'.format(highest_resonance_freq),
                     xy=(0.5, 0.95), xycoords='axes fraction',
                     ha='center', va='center',
                     bbox=dict(boxstyle='round', alpha=0.1),
                     fontsize=10)

        plt.tight_layout()
        plt.show()
    
    def rt60(self, audio_data, window_size=500):
        # Simple RT60 approximation
        rt60_values = []

        for i in range(0, len(audio_data), window_size):
            window = audio_data[i:i+window_size]
            envelope = np.abs(window)
            threshold = np.max(envelope) / np.exp(1)
            indices = np.where(envelope >= threshold)[0]
            if len(indices) >= 2:
                rt60_values.append(window[indices[-1]] - window[indices[0]])
            else:
                rt60_values.append(0.0)

        return rt60_values
        
    def plot_high(self, window_size=500):
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        
        plt.clf()
        # Compute RT60 values
        rt60_values = self.rt60(self.audio_array, window_size)

        # Plot RT60 values
        time_rt60 = np.arange(0, len(self.audio_array), window_size) / len(self.audio_array) * self.time_axis[-1]
        plt.plot(time_rt60, rt60_values, label='RT60', zorder=1)
        plt.title('RT60 Over Time of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.scatter([0.240], [5693], label='5693hz', color='red', zorder=2)
        tick_positions = np.arange(0, self.time_axis[-1], 0.5)
        plt.xticks(tick_positions)
        plt.legend()
                
        plt.tight_layout()
        plt.show()

    def plot_mid(self, window_size=500):
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        
        plt.clf()
        # Compute RT60 values
        rt60_values = self.rt60(self.audio_array, window_size)

        # Plot RT60 values
        time_rt60 = np.arange(0, len(self.audio_array), window_size) / len(self.audio_array) * self.time_axis[-1]
        plt.plot(time_rt60, rt60_values, label='RT60', zorder=1)
        plt.title('RT60 Over Time of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.scatter([0.645], [2353], label='2353hz', color='green', zorder=2)
        tick_positions = np.arange(0, self.time_axis[-1], 0.5)
        plt.xticks(tick_positions)
        plt.legend()

        plt.tight_layout()
        plt.show()

    def plot_low(self, window_size=500):
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        
        plt.clf()
        # Compute RT60 values
        rt60_values = self.rt60(self.audio_array, window_size)

        # Plot RT60 values
        time_rt60 = np.arange(0, len(self.audio_array), window_size) / len(self.audio_array) * self.time_axis[-1]
        plt.plot(time_rt60, rt60_values, label='RT60', zorder=1)
        plt.title('RT60 Over Time of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.scatter([1.417], [180], label='185hz', color='yellow', zorder=2)
        tick_positions = np.arange(0, self.time_axis[-1], 0.5)
        plt.xticks(tick_positions)
        plt.legend()

        plt.tight_layout()
        plt.show()
 
    def plot_combined(self, window_size=500):
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        
        plt.clf()
        # Compute RT60 values
        rt60_values = self.rt60(self.audio_array, window_size)

        # Plot RT60 values
        time_rt60 = np.arange(0, len(self.audio_array), window_size) / len(self.audio_array) * self.time_axis[-1]
        plt.plot(time_rt60, rt60_values, label='RT60', zorder=1)
        plt.title('RT60 Over Time of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.scatter([0.244], [5693], label='5693hz', color='red', zorder=2)
        plt.scatter([0.645], [2353], label='2353hz', color='green', zorder=2)
        plt.scatter([1.417], [180], label='185hz', color='yellow', zorder=2)
        tick_positions = np.arange(0, self.time_axis[-1], 0.5)
        plt.xticks(tick_positions)
        plt.legend()
        
        # Display difference to reach 0.5 seconds
        plt.annotate('Difference from 0.5(s): {}'.format('+0.27(s)'),
                     xy=(0.5, 0.95), xycoords='axes fraction',
                     ha='center', va='center',
                     bbox=dict(boxstyle='round', alpha=0.1),
                     fontsize=10)

        plt.tight_layout()
        plt.show()
        
    # Plot spectrogram
    def plot_choice(self):
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        
        plt.clf()
        sampling_rate, audio_data = wavfile.read(self.wave_file)
        
        # Compute the spectrogram
        frequencies, times, spectrogram_data = spectrogram(audio_data, fs=sampling_rate)

        # Plot the spectrogram
        plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data), shading='auto')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.title('Spectrogram of Audio File')
        plt.colorbar(label='Intensity [dB]')
        plt.show()
        
    def plot_alternating(self, count):
        if count == 0:
            self.plot_low()
        if count == 1:
            self.plot_mid()
        if count == 2:
            self.plot_high()