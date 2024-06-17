#import statements
import tkinter as tk
import pyttsx3

def speak_text():
    # Get text from entry widget
    text = entry.get()
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    
    # Convert text to speech
    engine.say(text)
    
    # Run the text-to-speech engine
    engine.runAndWait()

# Create the main window
window = tk.Tk()
window.title("Text-to-Speech Converter")

# Create a label
label = tk.Label(window, text="Enter text:")
label.pack()

# Create an entry widget
entry = tk.Entry(window, width=40)
entry.pack()

# Create a button
button = tk.Button(window, text="Speak", command=speak_text)
button.pack()

# Run the GUI
window.mainloop()
