import speech_recognition as sr
import pyaudio
import os

r = sr.Recognizer()

print("Speck Now")
def speek():
 with sr.Microphone() as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)

    except sr.UnknownValueError:
         print("sorry, Unknown Value Error")
         return
    except sr.RequestError:
         print("sorry, Request Error")
         return

speek()