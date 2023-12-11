import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

class FrequencyAnalyzer:
    def __init__(self, wav_file):
        self.sample_rate, self.data = wavfile.read(wav_file)
        self.freqs, self.t, self.spectrum = self.compute_spectrum()

    def find_target_frequency(self):
        for x in self.freqs:
            if x > 1000:
                break
        return x

    def frequency_check(self):
        print(self.freqs)
        target_frequency = self.find_target_frequency()
        index_of_frequency = np.where(self.freqs == target_frequency)[0][0]
        data_for_frequency = self.spectrum[index_of_frequency]
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun

    def compute_spectrum(self):
        _, _, spectrum = plt.specgram(self.data, Fs=self.sample_rate, NFFT=1024, noverlap=512, scale='dB')
        freqs, t, spectrum = np.fft.fftfreq(len(spectrum)), np.linspace(0, len(self.data) / self.sample_rate, len(spectrum)), np.transpose(spectrum)
        return freqs, t, spectrum

    def plot_rt60(self):
        data_in_db = self.frequency_check()

        plt.figure(2)
        plt.plot(self.t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
        plt.xlabel('Time (s)')
        plt.ylabel('Power (dB)')

        index_of_max = np.argmax(data_in_db)
        value_of_max = data_in_db[index_of_max]
        plt.plot(self.t[index_of_max], data_in_db[index_of_max], 'go')

        sliced_array = data_in_db[index_of_max:]
        value_of_max_less_5 = value_of_max - 5

        def find_nearest_value(array, value):
            array = np.asarray(array)
            idx = (np.abs(array - value)).argmin()
            return array[idx]

        value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
        index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
        plt.plot(self.t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
        plt.plot(self.t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')

        rt20 = (self.t[index_of_max_less_5] - self.t[index_of_max_less_25])[0]
        print(f'rt20 = {rt20}')
        rt60 = 3 * rt20
        plt.xlim(0, ((round(abs(rt60), 2)) * 1.5))
        plt.grid()

        plt.show()

        print(f'The RT60 reverb time at freq {int(self.find_target_frequency())}Hz is {round(abs(rt60), 2)} seconds')