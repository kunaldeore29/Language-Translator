import googletrans
from googletrans import Translator
from tkinter import *
from tkinter import messagebox, ttk
import speech_recognition as sr
from PIL import Image, ImageTk

# Initialize the translator
translator_object = Translator()
available_languages = googletrans.LANGUAGES

# Function to translate text
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
def clear():
    dest_language.set('')
    src_language.set('')
    text_entry.delete("1.0", "end")

# Function to listen for audio input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo(message="Listening...")
        audio = recognizer.listen(source)
        try:
            spoken_text = recognizer.recognize_google(audio)
            text_entry.delete("1.0", "end")
            text_entry.insert("1.0", spoken_text)
        except sr.UnknownValueError:
            messagebox.showerror(message="Could not understand audio")
        except sr.RequestError:
            messagebox.showerror(message="Could not request results from Google Speech Recognition service")

# Set up the main application window
window = Tk()
window.geometry("800x600")
window.title("Language Translator")
window.configure(bg="#f0f0f0")

# Load background image
bg_image = Image.open("background.jpg")  # Update with your image path
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to display the background image
canvas = Canvas(window, width=800, height=600)
canvas.pack(fill=BOTH, expand=True)

# Add the background image to the canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create a frame for better layout
frame = ttk.Frame(window, padding="60", style="Light.TFrame")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
style = ttk.Style()
style.configure("Light.TFrame", background="#d8e3bf")

# Title of the app
title_label = ttk.Label(frame, text="Language Translator", font=("Helvetica", 20), foreground="#333")
title_label.pack(pady=10)

# Text input
text_label = ttk.Label(frame, text="Text to translate:")
text_label.pack(anchor=W)
text_entry = Text(frame, width=50, height=5, font=("Ubuntu Mono", 12), wrap=WORD)
text_entry.pack(pady=5)

# Source language selection
src_label = ttk.Label(frame, text="Source language (empty: auto-detect):")
src_label.pack(anchor=W)
src_language = StringVar()
src_combobox = ttk.Combobox(frame, textvariable=src_language, values=list(available_languages.values()), font=("Ubuntu Mono", 12), width=20)
src_combobox.pack(pady=5)

# Destination language selection
dest_label = ttk.Label(frame, text="Target language (default: English):")
dest_label.pack(anchor=W)
dest_language = StringVar(value='english')  # Default to English
dest_combobox = ttk.Combobox(frame, textvariable=dest_language, values=list(available_languages.values()), font=("Ubuntu Mono", 12), width=20)
dest_combobox.pack(pady=5)

# Button frame
button_frame = ttk.Frame(frame)
button_frame.pack(pady=20)

translate_button = ttk.Button(button_frame, text='Translate', command=translate_function)
translate_button.grid(row=0, column=0, padx=10)

clear_button = ttk.Button(button_frame, text='Clear', command=clear)
clear_button.grid(row=0, column=1, padx=10)

listen_button = ttk.Button(button_frame, text='Speak', command=listen)
listen_button.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()
