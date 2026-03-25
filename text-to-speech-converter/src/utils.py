import pyttsx3

engine = pyttsx3.init()

def speak(text, volume=1.0, rate=150):
    engine.setProperty('volume', volume)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()
