########6 - Display the waveform from file - needs modified
import wave
import numpy as np
import matplotlib.pyplot as plt

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

        # Plot the waveform
        plt.plot(self.time_axis, self.audio_array)
        plt.title('Waveform of {}'.format(self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.show()

    def compute_highest_resonance(self):
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()

        # Perform frequency domain analysis using Fast Fourier Transform (FFT)
        spectrum = np.fft.fft(self.audio_array)
        frequencies = np.fft.fftfreq(len(spectrum), d=self.time_axis[1] - self.time_axis[0])

        # Find the index corresponding to the maximum amplitude (excluding DC component)
        max_index = np.argmax(np.abs(spectrum[1:])) + 1

        # Compute the corresponding frequency in Hz
        highest_resonance_freq = np.abs(frequencies[max_index])

        print('Highest Resonance Frequency: {:.2f} Hz'.format(highest_resonance_freq))
        
        # Define frequency ranges
        low_freq_range = (20, 200)
        mid_freq_range = (200, 2000)
        high_freq_range = (2000, 20000)

        # Find indices corresponding to each frequency range
        low_indices = np.where((frequencies >= low_freq_range[0]) & (frequencies <= low_freq_range[1]))[0]
        mid_indices = np.where((frequencies >= mid_freq_range[0]) & (frequencies <= mid_freq_range[1]))[0]
        high_indices = np.where((frequencies >= high_freq_range[0]) & (frequencies <= high_freq_range[1]))[0]

        # Compute the average amplitude in each frequency range
        low_amplitude = np.mean(np.abs(spectrum[low_indices]))
        mid_amplitude = np.mean(np.abs(spectrum[mid_indices]))
        high_amplitude = np.mean(np.abs(spectrum[high_indices]))

        print('Low-Frequency Amplitude: {:.2f} Hz'.format(np.abs(frequencies[low_indices[np.argmax(np.abs(spectrum[low_indices]))]])))
        print('Mid-Frequency Amplitude: {:.2f} Hz'.format(np.abs(frequencies[mid_indices[np.argmax(np.abs(spectrum[mid_indices]))]])))
        print('High-Frequency Amplitude: {:.2f} Hz'.format(np.abs(frequencies[high_indices[np.argmax(np.abs(spectrum[high_indices]))]])))