import os
import wave
import time
import threading
import tkinter as tk
import pyaudio


class AudioRecorder:

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.button = tk.Button(text="🎤", font=("Arial", 120, "bold"),
                                command=self.click_handler)

        self.button.pack()

        self.root.mainloop()


    def click_handler(self):
        pass