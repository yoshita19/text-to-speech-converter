from utils import speak

def main():
    print("Welcome to RESONATOR")

    speak("Welcome to RESONATOR")

    rate = 150

    while True:
        x = input("Enter text: ")

        if x.lower() == "bye":
            speak("Bye bye friend")
            break

        elif x.lower() == "fast":
            rate = 200
            speak("Now speaking fast", rate=rate)

        elif x.lower() == "slow":
            rate = 100
            speak("Now speaking slow", rate=rate)

        else:
            speak(x, rate=rate)

if __name__ == "__main__":
    main()
