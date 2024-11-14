import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError:
            print("Could not request results from the speech recognition service")
            return None