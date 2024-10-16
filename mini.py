# The code snippet you provided is importing necessary modules and libraries for the language
# translator application. Here is a breakdown of the imports:
import googletrans
from googletrans import Translator
from tkinter import *
from tkinter import messagebox, ttk
import speech_recognition as sr
from PIL import Image, ImageTk

# Initialize the translator
# The code `translator_object = Translator()` creates an instance of the `Translator` class from the
# `googletrans` module. This instance will be used to perform text translations in the language
# translator application.
translator_object = Translator()
available_languages = googletrans.LANGUAGES

# Function to translate text
"""
    The `translate_function` takes user input text, source language, and destination language to
    translate the text using a translator object, displaying the translated text or an error message.
    :return: The `translate_function` returns either an error message if an exception occurs during
    translation, or a message box displaying the translated text if the translation is successful.
    """
def translate_function():
    text_v = text_entry.get("1.0", "end-1c").strip()
    if len(text_v) == 0:
        messagebox.showerror(message="Enter valid text")
        return

    src_v = src_language.get() or 'en'# Default to English
    dest_v = dest_language.get() or None   
    try:
        translated_text = translator_object.translate(text_v, src=src_v, dest=dest_v)
        messagebox.showinfo(message="TRANSLATED TEXT: " + translated_text.text)
    except Exception as e:
        messagebox.showerror(message=f"Error: {str(e)}")

# Function to clear text fields
    """
    The `clear` function clears the selected destination and source languages and deletes the text entry
    content.
    """
def clear():
    dest_language.set('')
    src_language.set('')
    text_entry.delete("1.0", "end")

# Function to listen for audio input
    """
    The `listen` function uses the SpeechRecognition library in Python to listen for audio input from a
    microphone and transcribe it using Google's speech recognition service.
    """
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        #messagebox.showinfo(message="Please click on ok button :")
        audio = recognizer.listen(source)
        try:
            spoken_text = recognizer.recognize_google(audio)
            text_entry.delete("1.0", "end")
            text_entry.insert("1.0", spoken_text)
        except sr.UnknownValueError:
            messagebox.showerror(message="Could not understand audio")
        except sr.RequestError:
            messagebox.showerror(message="Could not request results Recognition service")

# Set up the main application window
# The code snippet `window = Tk()` creates the main application window using the Tkinter library in
# Python. Here's a breakdown of what each line does:
window = Tk()
window.geometry("800x600")
window.title("Language Translator")
window.configure(bg="#f0f0f0")

# This portion of the code is responsible for loading a background image and displaying it on a canvas
# within the main application window. Here's a breakdown of what each line does:
# Load background image
bg_image = Image.open("background.jpg") 
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to display the background image
canvas = Canvas(window, width=800, height=600)
canvas.pack(fill=BOTH, expand=True)

# Add the background image to the canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create a frame for better layout
# The code snippet you provided is creating a frame within the main application window using the
# `ttk.Frame` class from the `tkinter` library in Python. Here's a breakdown of what each line is
# doing:
frame = ttk.Frame(window, padding="90", style="Light.TFrame")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
style = ttk.Style()
style.configure("Light.TFrame", background="#2f6a8d")

# Title of the app-
# The code snippet you provided is creating a title label for the Language Translator application
# interface. Here's a breakdown of what each line is doing:
title_label = ttk.Label(frame, text="Language Translator", font=("Helvetica", 30), foreground="#141414",background="#2f6a8d")
title_label.pack(pady=10)

# Text input-
# The code snippet you provided is responsible for creating a text input field for users to enter the
# text they want to translate in the Language Translator application. Here's a breakdown of what each
# line is doing:
text_label = ttk.Label(frame, text="Text to translate:",font=("Ubuntu Mono", 13), foreground="#141414")
text_label.pack(anchor=W)
text_entry = Text(frame, width=50, height=5, font=("Ubuntu Mono", 12), wrap=WORD)
text_entry.pack(pady=5)

# Source language selection-
# The code snippet you provided is responsible for creating a section in the Language Translator
# application interface where users can select the source language for translation. Here's a breakdown
# of what each line is doing:
src_label = ttk.Label(frame, text="Source language (empty: auto-detect):",font=("Ubuntu Mono", 13), foreground="#141414")
src_label.pack(anchor=W)
src_language = StringVar()
src_combobox = ttk.Combobox(frame, textvariable=src_language, values=list(available_languages.values()), font=("Ubuntu Mono", 13), width=22)
src_combobox.pack(pady=5)

# Destination language selection-
# The code snippet you provided is responsible for creating a section in the Language Translator
# application interface where users can select the destination language for translation. Here's a
# breakdown of what each line is doing:
dest_label = ttk.Label(frame, text="Target language (default: English):",font=("Ubuntu Mono", 13), foreground="#141414")
dest_label.pack(anchor=W)
dest_language = StringVar(value='english')  # Default to English
dest_combobox = ttk.Combobox(frame, textvariable=dest_language, values=list(available_languages.values()), font=("Ubuntu Mono", 13), width=22)
dest_combobox.pack(pady=5)

# Button frame -
# The code snippet you provided is creating a frame within the main application window to organize
# buttons for different functions in the Language Translator application. Here's a breakdown of what
# each part of the code is doing:
button_frame = ttk.Frame(frame,width=30)
button_frame.pack(pady=10)

translate_button = ttk.Button(button_frame, text='Translate', command=translate_function)
translate_button.grid(row=0, column=0, padx=10)

clear_button = ttk.Button(button_frame, text='Clear', command=clear)
clear_button.grid(row=0, column=1, padx=10)

listen_button = ttk.Button(button_frame, text='Speak', command=listen)
listen_button.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()
