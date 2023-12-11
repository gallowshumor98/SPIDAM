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
        plt.tight_layout()
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
        
    
    def compute_rt60(self, frequency_range):
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()

        # Perform frequency domain analysis using Fast Fourier Transform (FFT)
        spectrum = np.fft.fft(self.audio_array)
        frequencies = np.fft.fftfreq(len(spectrum), d=self.time_axis[1] - self.time_axis[0])

        # Find indices corresponding to the specified frequency range
        indices = np.where((frequencies >= frequency_range[0]) & (frequencies <= frequency_range[1]))[0]

        # Extract amplitude in the specified frequency range
        amplitude = np.abs(spectrum[indices])

        # Estimate RT60 (reverberation time) as the time for the amplitude to decay to -60 dB
        threshold = np.max(amplitude) / np.sqrt(2)  # -60 dB is approximately 1/sqrt(2) times the max amplitude
        rt60_index = np.argmax(amplitude <= threshold)
        rt60_time = self.time_axis[indices[rt60_index]]

        return rt60_time

    def plot_rt60(self):
        frequencies = ['Low', 'Mid', 'High']
        low_rt60 = self.compute_rt60((20, 200))
        mid_rt60 = self.compute_rt60((200, 2000))
        high_rt60 = self.compute_rt60((2000, 20000))

        # Plot the RT60 values
        plt.bar(['Low', 'Mid', 'High'], [low_rt60, mid_rt60, high_rt60])
        plt.title('RT60 for Low, Mid, and High Frequencies')
        plt.xlabel('Frequency Range')
        plt.ylabel('RT60 (s)')
        plt.tight_layout()
        plt.show()