import os
import tkinter as tk
import datetime
import threading
from moviepy import VideoFileClip
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import ttk
import whisper

class whisper_converter:

    def __init__(self):
        #Window init
        self.root = tk.Tk()
        self.root.title('Whisper Transcriptor')
        self.root.resizable(False, False)
        self.root.geometry('400x150')

        #Widget Inits\
        self.open_button = ttk.Button(text='Open a File',command=self.t_window)
        self.progressbar = ttk.Progressbar()
        self.info_label = ttk.Label()

        #Vars
        self.filename = ''
        self.audio_filename = ''
        self.txt_filename = ''
        self.model= 'medium'
        self.language = 'German'
        self.result = '' 
        self.short_fname = ''
        self.date = ''

        self.open_button.pack(expand=True)
        self.info_label.place_forget()
        self.progressbar.place_forget()


        self.root.mainloop()

    def t_window(self):
        self.select_file()


        self.progressbar.place(x=50, y=50, width=300, height=50)
        self.short_fname = self.filename[self.filename.rfind('/') + 1:]
          
        self.info_label.config(text=f"Converting {self.short_fname} ...")
        self.progressbar.step(25)
        self.info_label.place(relx=0.5, y=120, anchor=tk.CENTER)

        conv_thread = threading.Thread(target=self.run_pipeline, daemon=True)
        conv_thread.start()

        return 0


    def select_file(self):
        filetypes = (
            ('Video files', '*.mp4'),)

        self.filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)

        self.progressbar.place(x=50, y=50, width=300, height=50)
        self.short_fname = self.filename[self.filename.rfind('/') + 1:]

        return 0


    def run_pipeline(self):

        #Threaded Pipeline so main window(root.mainloop) can stay active
        #and the Widgets (porgressbar & info_label) can get updated.
        
        self.mp4_conv()
        self.root.after(0, lambda: self.progressbar.step(50))

        self.root.after(0, lambda: self.info_label.config(text="Transcribing ..."))
        self.transcribe()
        self.root.after(0, lambda: self.progressbar.step(90))

        self.write_file()

        self.root.after(0, self.on_pipeline_done)

    def on_pipeline_done(self):
        #Garbage remover
        #removing of audio file could be made optional in future
        
        os.remove(self.audio_filename)
        self.progressbar.place_forget()
        self.info_label.place_forget()


    def mp4_conv(self):
        video = VideoFileClip(self.filename)
        self.audio_filename = str(datetime.datetime.now())
        self.audio_filename = self.audio_filename.replace(":","-")
        self.audio_filename = self.audio_filename[:19]
        self.date = self.audio_filename
        self.audio_filename = os.path.abspath(self.audio_filename)
        self.txt_filename = self.audio_filename
        print(self.audio_filename)


        if os.path.exists(f"{self.audio_filename}.mp3"):
            exists = True
            i = 1
            while exists:
                if os.path.exists(f"{self.audio_filename}_{i}.mp3"):
                    i += 1
                else:
                    exists = False
                    self.audio_filename = f"{self.audio_filename}_{i}.mp3"
        else:
            self.audio_filename = f"{self.audio_filename}.mp3"
        video.audio.write_audiofile(self.audio_filename)

        return 0

    def transcribe(self):
        model = whisper.load_model(self.model)

        self.result = model.transcribe(self.audio_filename)
        return 0

    def write_file(self):
        
        if os.path.exists(f"{self.txt_filename}.txt"):
            exists = True
            i = 1
            while exists:
                if os.path.exists(f"{self.txt_filename}_{i}.txt"):
                    i += 1
                else:
                    exists = False
                    self.txt_filename = f"{self.txt_filename}_{i}.txt"
        else:
            self.txt_filename = f"{self.txt_filename}.txt"
  
        with open(self.txt_filename, "w", encoding="utf-8") as f:
            f.write(f"Meeting from {self.date}\n")

            txts = self.result['text'].split('.')

            for txt in txts:
                f.write(f"{txt}\n")

        f.close()

        return 0





# run the application
whisper_converter()
