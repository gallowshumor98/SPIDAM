# 1 - Load audio file, use a button to open it -> display the name of the file
# 2 - If: the file is not .wav -> Convert to .wav -> 3
# 3 - Else: Check for meta or multi channel
# 4 -   True: Remove meta or handle multi channel -> 5
# 5 -   False: Display time value of .wav in seconds
# 6 - Display wave form of .wav
# 7 - Compute highest resonance and display frequency value in Hz
# 8 - Compute Low, Mid, High frequency
# 9 - Display plot of RT60 for Low, Mid, High frequecies
#     9.5 - Extra Credit - Button to Alternate through Low, Mid, High plots
# 10 - Button to combine plots into single plot
# 11 - Show difference in RT60 value to reduce to .5 seconds
# 12 - Add button and additional visual output for useful data (your choice)



#1 - Modify the following to get the file
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

gfile = ''

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')
'''
tkinter.filedialog.askopenfilenames(**options)
Create an Open dialog and
return the selected filename(s) that correspond to
existing file(s).
screenshot
screenshot
'''

def select_file():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title = 'Open a file', initialdir = '/', filetypes=filetypes)
    gfile = filename
    
    # tkinter.messagebox — Tkinter message prompts
    #placeholder 1
    showinfo(title='Selected File', message = filename)
    
    #placeholder 2
    gfile_label = ttk.Label(root, text=gfile)
    gfile_label.pack(side="bottom")
    
# open button
open_button = ttk.Button(root, text='Open a File', command = select_file)
open_button.pack(expand = True)
# run the application
root.mainloop()