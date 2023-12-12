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
        # See if audio file is empty
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        # Clear graph of previous plots
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
        # Plots the RT60 and displays a scatter of the highest amplitude
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        # Clear graph of previous plots
        plt.clf()
        # Compute RT60 values
        rt60_values = self.rt60(self.audio_array, window_size)
        # Plot RT60 values
        time_rt60 = np.arange(0, len(self.audio_array), window_size) / len(self.audio_array) * self.time_axis[-1]

        # Find the index and value of the maximum amplitude
        max_index = np.argmax(rt60_values)
        max_amplitude = rt60_values[max_index]

        # Plot graph
        plt.plot(time_rt60, rt60_values, label='RT60', zorder=1)
        plt.title('RT60 Over Time of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.scatter([time_rt60[max_index]], [max_amplitude], label='Highest Frequency: {:.2f} Hz'.format(max_amplitude), color='red', zorder=2)
        tick_positions = np.arange(0, self.time_axis[-1], 0.5)
        plt.xticks(tick_positions)
        plt.legend()

        plt.tight_layout()
        plt.show()

    def plot_mid(self, window_size=500):
        # Plots the RT60 and displays a scatter of the median amplitude
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        # Clear graph of previous plots
        plt.clf()
        # Compute RT60 values
        rt60_values = self.rt60(self.audio_array, window_size)

        # Find the index and value of the maximum amplitude
        max_index = np.argmax(rt60_values)
        max_amplitude = rt60_values[max_index]

        # Find indices where RT60 values are positive
        positive_indices = np.where(np.array(rt60_values) > 0)[0]
        # Extract positive RT60 values
        positive_rt60_values = np.array(rt60_values)[positive_indices]
        # Find the index and value of the lowest positive RT60
        min_index = positive_indices[np.argmin(positive_rt60_values)]
        min_amplitude = np.min(positive_rt60_values)

        # Find the index and value of the mid amplitude
        median_amplitude = (min_amplitude + max_amplitude) / 2
        median_index = np.argmin(np.abs(positive_rt60_values - median_amplitude))


        # Plot RT60 values
        time_rt60 = np.arange(0, len(self.audio_array), window_size) / len(self.audio_array) * self.time_axis[-1]
        
        
        # Plot graph
        plt.plot(time_rt60, rt60_values, label='RT60', zorder=1)
        plt.title('RT60 Over Time of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.scatter([time_rt60[median_index]], [median_amplitude], label='Median Frequency: {:.2f} Hz'.format(median_amplitude), color='green', zorder=2)
        tick_positions = np.arange(0, self.time_axis[-1], 0.5)
        plt.xticks(tick_positions)
        plt.legend()

        plt.tight_layout()
        plt.show()

    def plot_low(self, window_size=500):
        # Plots the RT60 and displays a scatter of the lowest amplitude
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        # Clear graph of previous plots
        plt.clf()
        # Compute RT60 values
        rt60_values = self.rt60(self.audio_array, window_size)
        
        # Find indices where RT60 values are positive
        positive_indices = np.where(np.array(rt60_values) > 0)[0]
        # Extract positive RT60 values
        positive_rt60_values = np.array(rt60_values)[positive_indices]
        # Find the index and value of the lowest positive RT60
        min_index = positive_indices[np.argmin(positive_rt60_values)]
        min_amplitude = np.min(positive_rt60_values)


        # Plot RT60 values
        time_rt60 = np.arange(0, len(self.audio_array), window_size) / len(self.audio_array) * self.time_axis[-1]
        plt.plot(time_rt60, rt60_values, label='RT60', zorder=1)
        plt.title('RT60 Over Time of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.scatter([time_rt60[min_index]], [min_amplitude], label='Lowest Frequency: {:.2f} Hz'.format(min_amplitude), color='yellow', zorder=2)
        tick_positions = np.arange(0, self.time_axis[-1], 0.5)
        plt.xticks(tick_positions)
        plt.legend()

        plt.tight_layout()
        plt.show()
 
    def plot_combined(self, window_size=500):
        # Plots the RT60 and displays a scatter of the high, median, and low amplitudes
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        # Clear graph of previous plots
        plt.clf()
        # Compute RT60 values
        rt60_values = self.rt60(self.audio_array, window_size)

        # Plot RT60 values
        time_rt60 = np.arange(0, len(self.audio_array), window_size) / len(self.audio_array) * self.time_axis[-1]
        
        # Find the index and value of the maximum amplitude
        max_index = np.argmax(rt60_values)
        max_amplitude = rt60_values[max_index]
        # Find the index and value of the maximum amplitude
        max_index = np.argmax(rt60_values)
        max_amplitude = rt60_values[max_index]

        # Find indices where RT60 values are positive
        positive_indices = np.where(np.array(rt60_values) > 0)[0]
        # Extract positive RT60 values
        positive_rt60_values = np.array(rt60_values)[positive_indices]
        # Find the index and value of the lowest positive RT60
        min_index = positive_indices[np.argmin(positive_rt60_values)]
        min_amplitude = np.min(positive_rt60_values)

        # Find the index and value of the mid amplitude
        median_amplitude = (min_amplitude + max_amplitude) / 2
        median_index = np.argmin(np.abs(positive_rt60_values - median_amplitude))

        
        # Plot graph
        plt.plot(time_rt60, rt60_values, label='RT60', zorder=1)
        plt.title('RT60 Over Time of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.scatter([time_rt60[max_index]], [max_amplitude], label='Highest Frequency: {:.2f} Hz'.format(max_amplitude), color='red', zorder=2)
        plt.scatter([time_rt60[median_index]], [median_amplitude], label='Median Frequency: {:.2f} Hz'.format(median_amplitude), color='green', zorder=2)
        plt.scatter([time_rt60[min_index]], [min_amplitude], label='Lowest Frequency: {:.2f} Hz'.format(min_amplitude), color='yellow', zorder=2)
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
        # Choice was to plot the spectrogram of the audio file
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        # Clear graph of previous plots
        plt.clf()
        sampling_rate, audio_data = wavfile.read(self.wave_file)
        
        # Compute the spectrogram
        frequencies, times, spectrogram_data = spectrogram(audio_data, fs=sampling_rate)

        # Plot the graph
        plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data), shading='auto')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.title('Spectrogram of Audio File')
        plt.colorbar(label='Intensity [dB]')
        plt.show()
        
    def plot_alternating(self, count):
        # Alternates displaying RT60 with high, median, or low amplitude
        if count == 0:
            self.plot_low()
        if count == 1:
            self.plot_mid()
        if count == 2:
            self.plot_high()