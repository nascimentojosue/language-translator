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

def translate_text(text, target_language='es'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text

def speak_text(text, language='es'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("translated_audio.mp3")
    os.system("start translated_audio.mp3" if os.name == "nt" else "mpg123 translated_audio.mp3")
