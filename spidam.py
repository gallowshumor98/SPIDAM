#### Complete GUI - Load audio file, use a button to open it -> display the name of the file
#### Implement processAudio.py -- Complete
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

##### GUI
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
root.geometry('275x200')

def select_file():
    global gfile
    global plot_button

    filetypes = (('All files', '*.*'), ('WAV files', '*.wav'), ('MP3 files', '*.mp3'), ('AAC files', '*.aac'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    gfile = filename

    # Process the audio file
    #Convert to wav - Complete
    if gfile.lower().endswith(('.mp3', '.aac')):
        audio_processor = AudioProcessor(gfile, os.path.splitext(gfile)[0] + '_converted.wav')
        audio_processor.process()
        gfile = audio_processor.output_file  # Update gfile with the converted file path
    
    
    # Update label with the selected file path
    gfile_label.config(text=gfile)

    # Enable the 'Plot' button
    plot_button.config(state="normal")
    low_button.config(state="normal")
    mid_button.config(state="normal")
    high_button.config(state="normal")
    combined_button.config(state="normal")
    other_button.config(state="normal")
    
    # Show selected file in messagebox
    showinfo(title='Selected File', message=gfile)

def plot_data():
    sound_display = WaveformPlotter(gfile)  
    sound_display.plot_waveform()
   # sound_display.compute_highest_resonance()
    
def process_low():
    # Placeholder for processing audio for the 'Low' action
    showinfo(title='Audio Processing', message='Processing audio for action: Low')

# Open button
open_button = ttk.Button(root, text='Open a File', command=select_file)
open_button.grid(row=0, column=1, pady=5, padx=5, sticky='ew')

# Label to display the selected file path
gfile_label = ttk.Label(root, text=gfile)
gfile_label.grid(row=1, column=0, columnspan=3, pady=5, padx=5, sticky='ew')

# Plot button (initially disabled)
plot_button = ttk.Button(root, text='Waveform', command=plot_data, state="disabled")
plot_button.grid(row=4, column=1, columnspan=1, pady=5, padx=5, sticky='ew')

low_button = ttk.Button(root, text='Low', command=process_low, state="disabled")
low_button.grid(row=3, column=0, columnspan=1, pady=5, padx=5, sticky='ew')

mid_button = ttk.Button(root, text='Mid', command=process_low, state="disabled")
mid_button.grid(row=3, column=1, columnspan=1, pady=5, padx=5, sticky='ew')

high_button = ttk.Button(root, text='High', command=process_low, state="disabled")
high_button.grid(row=3, column=2, columnspan=1, pady=5, padx=5, sticky='ew')

combined_button = ttk.Button(root, text='Combined', command=process_low, state="disabled")
combined_button.grid(row=4, column=0, columnspan=1, pady=5, padx=5, sticky='ew')

other_button = ttk.Button(root, text='Other', command=process_low, state="disabled")
other_button.grid(row=4, column=2, columnspan=1, pady=5, padx=5, sticky='ew')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Run the application
root.mainloop()
###### End GUI

