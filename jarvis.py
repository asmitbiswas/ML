
import datetime
import urllib.parse
import webbrowser

import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
engine.setProperty("rate", 175)

recognizer = sr.Recognizer()


def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        command = recognizer.recognize_google(audio)
        print(f"You: {command}")
        return command.lower()

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""

    except sr.RequestError:
        speak("Speech recognition requires an internet connection.")
        return ""

    except OSError:
        speak("I cannot access your microphone.")
        return ""


def execute(command):
    if not command:
        return True

    if "hello" in command or "hey jarvis" in command:
        speak("Hello, boss. All systems are ready.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {current_date}.")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    elif "search for" in command:
        query = command.split("search for", 1)[1].strip()

        if query:
            speak(f"Searching Google for {query}.")
            url = (
                "https://www.google.com/search?q="
                + urllib.parse.quote(query)
            )
            webbrowser.open(url)
        else:
            speak("What should I search for?")

    elif "who are you" in command:
        speak("I am Jarvis, your personal Python assistant.")

    elif "your name" in command:
        speak("My name is Jarvis.")

    elif "help" in command:
        speak(
            "You can ask for the time or date, "
            "open YouTube, Google, or GitHub, "
            "search Google, or ask who I am."
        )

    elif "shutdown jarvis" in command or "exit jarvis" in command:
        speak("Shutting down. Goodbye, boss.")
        return False

    else:
        speak("I don't know that command yet.")

    return True


def main():
    speak("Initializing JARVIS.")
    speak("Hello, boss. Systems online.")

    while True:
        command = listen()

        if not execute(command):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("JARVIS shutting down. Goodbye, boss.")