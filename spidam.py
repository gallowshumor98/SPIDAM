from soundDisplay import WaveformPlotter
from processAudio import AudioProcessor
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Initiate global references
gfile = ''
count = 0
plot_button = None  # Global reference to the 'Plot' button

# create the root window
root = tk.Tk()
root.title('Audio File Selection')
root.resizable(False, False)
root.geometry('275x200')


def select_file():
    #Method to select an audio file
    global gfile
    global plot_button

    filetypes = (('All files', '*.*'), ('WAV files', '*.wav'), ('MP3 files', '*.mp3'), ('AAC files', '*.aac'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    gfile = filename

    # Process the audio fileand convert to wav
    if gfile.lower().endswith(('.mp3', '.aac')):
        audio_processor = AudioProcessor(gfile, os.path.splitext(gfile)[0] + '_converted.wav')
        audio_processor.process()
        gfile = audio_processor.output_file  # Update gfile with the converted file path
    
    
    # Update label with the selected file path
    gfile_label.config(text=gfile)

    # Enable the functionality buttons that are dependent on a file being selected
    plot_button.config(state="normal")
    low_button.config(state="normal")
    mid_button.config(state="normal")
    high_button.config(state="normal")
    combined_button.config(state="normal")
    other_button.config(state="normal")
    alt_button.config(state="normal")
    
    # Show selected file in messagebox
    showinfo(title='Selected File', message=gfile)

# Create instance and display waveform
def plot_data():
    sound_display = WaveformPlotter(gfile)  
    sound_display.plot_waveform()

# Create instance and display high frequency of RT60
def high():
    sound_display = WaveformPlotter(gfile)  
    sound_display.plot_high()

# Create instance and display low frequency of RT60
def low():
    sound_display = WaveformPlotter(gfile)  
    sound_display.plot_low()

# Create instance and display median frequency of RT60
def mid():
    sound_display = WaveformPlotter(gfile)  
    sound_display.plot_mid()

# Create instance and display high, mid, and low frequencies of RT60
def combined():
    sound_display = WaveformPlotter(gfile)  
    sound_display.plot_combined()

# Create instance and display spectrogram of audio file
def choice():
    sound_display = WaveformPlotter(gfile)
    sound_display.plot_choice()

# Create instance and alternate between high, mid, and low
def alternate():
    global count
    sound_display = WaveformPlotter(gfile)
    sound_display.plot_alternating(count)
    count += 1
    if count == 3:
        count = 0


# Open button
open_button = ttk.Button(root, text='Open a File', command=select_file)
open_button.grid(row=0, column=1, pady=5, padx=5, sticky='ew')

# Label to display the selected file path
gfile_label = ttk.Label(root, text=gfile)
gfile_label.grid(row=1, column=0, columnspan=3, pady=5, padx=5, sticky='ew')

# Plot button (initially disabled)
plot_button = ttk.Button(root, text='Waveform', command=plot_data, state="disabled")
plot_button.grid(row=4, column=1, columnspan=1, pady=5, padx=5, sticky='ew')

# Low button (initially disabled)
low_button = ttk.Button(root, text='Low', command=low, state="disabled")
low_button.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky='ew')

# Mid button (initially disabled)
mid_button = ttk.Button(root, text='Mid', command=mid, state="disabled")
mid_button.grid(row=3, column=1, columnspan=1, pady=5, padx=5, sticky='ew')

# High button (initially disabled)
high_button = ttk.Button(root, text='High', command=high, state="disabled")
high_button.grid(row=3, column=2, columnspan=1, pady=5, padx=5, sticky='ew')

# Combined button (initially disabled)
combined_button = ttk.Button(root, text='Combined', command=combined, state="disabled")
combined_button.grid(row=4, column=0, columnspan=1, pady=5, padx=5, sticky='ew')

# Other button (initially disabled)
other_button = ttk.Button(root, text='Spectrogram', command=choice, state="disabled")
other_button.grid(row=4, column=2, columnspan=1, pady=5, padx=5, sticky='ew')

# Alternating button (initially disabled)
alt_button = ttk.Button(root, text='Alternate', command=alternate, state="disabled")
alt_button.grid(row=5, column=1, columnspan=1, pady=5, padx=5, sticky='ew')

# Lock columns in place
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Run the application
root.mainloop()

