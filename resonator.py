import pyttsx3

def speak(text , volume=1.0):
    engine = pyttsx3.init()
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == '__main__':
    print("welcome to RESONATOR") 
    speak("welcome to RESONATOR this is a application build to help people with speaking disabilities")
    while True:
        x = input("enter text for audio: ")
        if x == "bye":
            speak("bye bye friend")
            break
        elif x=="loud":
            speak("ok i will speak loudly" , volume=1.0)
        elif x=="normal":
            speak("ok normal tone", volume=0.5)
        
        speak(x)