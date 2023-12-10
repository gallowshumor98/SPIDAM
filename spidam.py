#### Done in GUI 1 - Load audio file, use a button to open it -> display the name of the file

#### Implement processAudio.py
# Check if wav
#    If mp3 or aac -> Convert to wav
# Check if has meta or multi channel
#    If yes -> remove meta or handle multi channel

#### After processing, display wave form of wav file
# Compute highest resonance and display frequency value in Hz
# Compute Low, Mid, High frequency
# Display plot of RT60 for Low, Mid, High frequecies
#      Extra Credit - Button to Alternate through Low, Mid, High plots
# Button to combine plots into single plot
# Show difference in RT60 value to reduce to .5 seconds
# Add button and additional visual output for useful data (your choice)

##### GUI - Trying to Implement
# main.py
from soundDisplay import WaveformPlotter
from processAudio import AudioProcessor
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

gfile = ''
plot_button = None  # Global reference to the 'Plot' button

# create the root window
root = tk.Tk()
root.title('Audio File Selection')
root.resizable(False, False)
root.geometry('300x150')

def select_file():
    global gfile
    global plot_button

    filetypes = (('WAV files', '*.wav'), ('MP3 files', '*.mp3'), ('AAC files', '*.aac'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    gfile = filename

    # Process the audio file
    #Convert to wav - Complete
    if gfile.lower().endswith(('.mp3', '.aac')):
        audio_processor = AudioProcessor(gfile, os.path.splitext(gfile)[0] + '_converted.wav')
        audio_processor.convert_to_wav()
        gfile = audio_processor.output_file  # Update gfile with the converted file path

    # Update label with the selected file path
    gfile_label.config(text=gfile)

    # Enable the 'Plot' button
    plot_button.config(state="normal")

    # Show selected file in messagebox
    showinfo(title='Selected File', message=gfile)

def plot_data():
    sound_display = WaveformPlotter(gfile)
    sound_display.plot_waveform()
    sound_display.compute_highest_resonance()

# Open button
open_button = ttk.Button(root, text='Open a File', command=select_file)
open_button.pack(expand=True)

# Label to display the selected file path
gfile_label = ttk.Label(root, text=gfile)
gfile_label.pack(side="bottom")

# Plot button (initially disabled)
plot_button = ttk.Button(root, text='Plot', command=plot_data, state="disabled")
plot_button.pack(expand=True)

# Run the application
root.mainloop()
###### End GUI




########6 - Display the wave from file - needs modified
# audioSpectrum mono only
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile
# sample_rate, data = wavfile.read('16bitmono.wav')
# spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, \
# NFFT=1024, cmap=plt.get_cmap('autumn_r'))
# cbar = plt.colorbar(im)
# plt.xlabel('Time (s)')
# plt.ylabel('Frequency (Hz)')
# cbar.set_label('Intensity (dB)')
# plt.show()
#######1 - Modify the following to get the file
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo

# gfile = ''

# create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')
'''
tkinter.filedialog.askopenfilenames(**options)
Create an Open dialog and
return the selected filename(s) that correspond to
existing file(s).
screenshot
screenshot
'''

# def select_file():
    # filetypes = (('MP3 files', '*.mp3'), ('AAC files', '*.aac'), ('WAV files', '*.wav'), ('All files', '*.*'))
    # filename = fd.askopenfilename(title = 'Open a file', initialdir = '/', filetypes=filetypes)
    # gfile = filename
    
    # tkinter.messagebox — Tkinter message prompts
    #placeholder 1
    # showinfo(title='Selected File', message = filename)
    
    #placeholder 2
    # gfile_label = ttk.Label(root, text=gfile)
    # gfile_label.pack(side="bottom")
    
# open button
# open_button = ttk.Button(root, text='Open a File', command = select_file)
# open_button.pack(expand = True)
# run the application
# root.mainloop()

####### 2 - If: the file is not .wav (aac or mp3) -> Convert to .wav -> 3

### mp3 to wav
# from pydub import AudioSegment

# def convert_mp3_to_wav(mp3_file, wav_file):
    # Load the MP3 file
    # audio = AudioSegment.from_mp3(mp3_file)

    # Export the audio to WAV format
    # audio.export(wav_file, format="wav")

# Example usage
# mp3_file_path = "input.mp3"
# wav_file_path = "output.wav"

# convert_mp3_to_wav(mp3_file_path, wav_file_path)

### aac to wav
# from pydub import AudioSegment

# def convert_aac_to_wav(aac_file, wav_file):
    # Load the AAC file
    # audio = AudioSegment.from_file(aac_file, format="aac")

    # Export the audio to WAV format
    # audio.export(wav_file, format="wav")

# Example usage
# aac_file_path = "input.aac"
# wav_file_path = "output.wav"

# convert_aac_to_wav(aac_file_path, wav_file_path)


########6 - Display the wave from file - needs modified
# audioSpectrum mono only
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile
# sample_rate, data = wavfile.read('16bitmono.wav')
# spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, \
# NFFT=1024, cmap=plt.get_cmap('autumn_r'))
# cbar = plt.colorbar(im)
# plt.xlabel('Time (s)')
# plt.ylabel('Frequency (Hz)')
# cbar.set_label('Intensity (dB)')
# plt.show()

# ReverbTime 0
# From Lec 25 slides

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile

# sample_rate, data = wavfile.read("filename.wav")

# select a frequency under 1kHz
# def find_target_freqeuncy(freqs):
    # for x in freqs:
        # if x > 1000:
            # break
    # return x

# def frequency_check():
    # identify a frequency to check
    # print(freqs)
    # global target_frequency
    # target_frequency = find_target_freqeuncy(freqs)
    # index_of_frequency = np.where(freqs == target_frequency)[0][0]
    # find sound data for a particular frequency
    # data_for_frequency = spectrum[index_of_frequency]
    # change a digital signal for a value in decibels
    # data_in_db_fun = 10 * np.log10(data_for_frequency)
    # return data_in_db_fun

# data_in_db = frequency_check()
# plt.figure(2)

# plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')

# plt.xlabel('Time (s)')
# plt.ylabel('Power (dB)')

# find an index of maxvalue
# index_of_max = np.argmax(data_in_db)
# value_of_max = data_in_db[index_of_max]
# plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

# slice our array from a max value
# sliced_array = data_in_db[index_of_max:]
# value_of_max_less_5 = value_of_max - 5

# find a nearest value of less 5db
# def find_nearest_value(array, value):
    # array = np.asarray(array)
    # idx = (np.abs(array - value)).argmin()
    # return array[idx]

# value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
# index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
# plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

# slice array from max-5dB
# value_of_max_less_25 = value_of_max - 25
# value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
# index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
# plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')

# rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]
# print(f'rt20 = {rt20}')
# rt60 = 3 * rt20
# plt.xlim(0, ((round(abs(rt60), 2)) * 1.5))
# plt.grid()

# plt.show()

# print(f'The RT60 reverb time at freq {int(target_frequency)}Hz is {round(abs(rt60), 2)} seconds')
