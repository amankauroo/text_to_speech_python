import tkinter as tk
from tkinter import Scrollbar, Text
import pyttsx3

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text-to-Speech App")

        self.text_entry = Text(master, wrap=tk.WORD, height=10, width=40)
        self.text_entry.pack(pady=10)

        self.scrollbar = Scrollbar(master, command=self.text_entry.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_entry.config(yscrollcommand=self.scrollbar.set)

        self.speak_button = tk.Button(master, text="Speak", command=self.speak_text)
        self.speak_button.pack(pady=10)

        self.engine = pyttsx3.init()

    def speak_text(self):
        text_to_speak = self.text_entry.get("1.0", tk.END).strip()
        if text_to_speak:
            self.engine.say(text_to_speak)
            self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
