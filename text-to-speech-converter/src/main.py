from utils import speak, set_voice

def main():
    print("Welcome to RESONATOR")

    speak("Welcome to RESONATOR. This application helps people with speaking disabilities.")

    while True:
        x = input("Enter text for audio: ")

        if x.lower() == "bye":
            speak("Bye bye friend")
            break

        elif x.lower() == "loud":
            speak("Ok I will speak loudly", volume=1.0)

        elif x.lower() == "normal":
            speak("Ok normal tone", volume=0.5)

        else:
            speak(x)

if __name__ == "__main__":
    main()