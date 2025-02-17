import speech_recognition as sr
import os

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
    with open("speech.txt", "w") as file:
        file.write(text)
    print("Speech saved to speech.txt")
except:
    print("Could not recognize speech.")

