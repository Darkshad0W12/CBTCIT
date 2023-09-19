import sounddevice as sd
from tkinter import *
import queue
import soundfile as sf
import threading
from tkinter import messagebox
from tkinter import ttk  # Import ttk for styled buttons

# Functions to play, stop, and record audio in Python voice recorder
def threading_rec(x):
    if x == 1:
        # If recording is selected, then the thread is activated
        t1 = threading.Thread(target=record_audio)
        t1.start()
    elif x == 2:
        # To stop, set the flag to false
        global recording
        recording = False
        messagebox.showinfo(message="Recording finished")
    elif x == 3:
        # To play a recording, it must exist.
        if file_exists:
            # Read the recording if it exists and play it
            data, fs = sf.read("trial.wav", dtype='float32')
            sd.play(data, fs)
            sd.wait()
        else:
            # Display an error if none is found
            messagebox.showerror(message="Record something to play")


# Recording function
def record_audio():
    # Declare global variables
    global recording
    # Set to True to record
    recording = True
    global file_exists
    # Create a file to save the audio
    messagebox.showinfo(message="Recording Audio. Speak into the mic")
    with sf.SoundFile("trial.wav", mode='w', samplerate=44100,
                      channels=2) as file:
        # Create an input stream to record audio without a preset time
        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            while recording:
                # Set the variable to True to allow playing the audio later
                file_exists = True
                # Write into file
                file.write(q.get())


# Define the user interface for Voice Recorder using Python
voice_rec = Tk()
voice_rec.title("V-O-I-C-E")
voice_rec.config(bg="#1295a1")

# Create a queue to contain the audio data
q = queue.Queue()

# Declare variables and initialize them
recording = False
file_exists = False

# Label to display app title in Python Voice Recorder Project
title_lbl = Label(voice_rec, text="V-O-I-C-E", bg="#a9d8d9", font=("Arial", 20))
title_lbl.pack(fill="x", pady=(10, 20))

# Use ttk buttons for a more realistic look
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
record_btn = ttk.Button(voice_rec, text="Record Audio", command=lambda m=1: threading_rec(m))
stop_btn = ttk.Button(voice_rec, text="Stop Recording", command=lambda m=2: threading_rec(m))
play_btn = ttk.Button(voice_rec, text="Play Recording", command=lambda m=3: threading_rec(m))

# Pack buttons and center them
record_btn.pack(side="left", fill="both", expand=True, padx=10)
stop_btn.pack(side="left", fill="both", expand=True, padx=10)
play_btn.pack(side="left", fill="both", expand=True, padx=10)

voice_rec.geometry("480x240")  # Set window size

voice_rec.mainloop()
