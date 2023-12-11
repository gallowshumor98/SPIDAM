########6 - Display the waveform from file
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
    
    def plot_high(self, threshold=2000)
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()
        
        # Perform frequency domain analysis using Fast Fourier Transform (FFT)
        spectrum = np.fft.fft(self.audio_array)
        frequencies = np.fft.fftfreq(len(spectrum), d=self.time_axis[1] - self.time_axis[0])
        
        # Find the indices corresponding to high frequencies
        high_freq_indices = np.where(np.abs(frequencies) > threshold)[0]

        # Plot a scatter plot of high frequencies
        plt.scatter(self.time_axis[high_freq_indices], np.abs(self.audio_array[high_freq_indices]))
        plt.title('High Frequencies (above {} Hz) of {}'.format(threshold, self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.show()
    
    def plot_mid(self, low_threshold=200, high_threshold=1999)
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()

        # Perform frequency domain analysis using Fast Fourier Transform (FFT)
        spectrum = np.fft.fft(self.audio_array)
        frequencies = np.fft.fftfreq(len(spectrum), d=self.time_axis[1] - self.time_axis[0])
        
        # Find the indices corresponding to mid frequencies
        mid_freq_indices = np.where(np.abs(frequencies) > low_threshold)[0] and (np.abs(frequencies) < high_threshold)[0]

        # Plot a scatter plot of mid frequencies
        plt.scatter(self.time_axis[high_freq_indices], np.abs(self.audio_array[high_freq_indices]))
        plt.title('Mid Frequencies (above {} Hz) of {}'.format(low_threshold, self.wave_file))
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.show()
    
    def plot_low(self, high_threshold=199)
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()

        # Perform frequency domain analysis using Fast Fourier Transform (FFT)
        spectrum = np.fft.fft(self.audio_array)
        frequencies = np.fft.fftfreq(len(spectrum), d=self.time_axis[1] - self.time_axis[0])
    
    def plot_choice(self)
        if self.audio_array is None or self.time_axis is None:
            self.read_wave_file()

        # Perform frequency domain analysis using Fast Fourier Transform (FFT)
        spectrum = np.fft.fft(self.audio_array)
        frequencies = np.fft.fftfreq(len(spectrum), d=self.time_axis[1] - self.time_axis[0])