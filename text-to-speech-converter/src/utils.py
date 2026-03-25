import pyttsx3

engine = pyttsx3.init()

def speak(text, volume=1.0):
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()

def set_voice(rate=None):
    if rate:
        engine.setProperty('rate', rate)