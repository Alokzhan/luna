import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import subprocess

# Initialize pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(audio):
    """Function to speak the given text."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Function to greet the user based on the time of the day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Luna, Sir. Please tell me how may I help you.")

def takeCommand():
    """Function to take voice input from the user and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Microphone timeout, please try again.")
        except sr.UnknownValueError:
            print("Could not understand audio, please repeat.")
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
        return "none"

def playYouTubeVideo(search_query):
    """Function to search and play a video on YouTube."""
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    speak(f"Playing {search_query} on YouTube.")

def openWebsite(name):
    """Function to open popular websites based on voice command."""
    websites = {
        "instagram": "https://www.instagram.com",
        "twitter": "https://www.twitter.com",
        "linkedin": "https://www.linkedin.com",
        "github": "https://www.github.com",
        "facebook": "https://www.facebook.com"
    }
    if name in websites:
        webbrowser.open(websites[name])
        speak(f"Opening {name}.")
    else:
        speak(f"Sorry, I don't know how to open {name}.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'open youtube' in query:
            speak("What should I play on YouTube?")
            search_query = takeCommand()
            playYouTubeVideo(search_query)

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results for this query. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("No results found on Wikipedia.")

        elif 'open instagram' in query:
            openWebsite("instagram")

        elif 'open twitter' in query:
            openWebsite("twitter")

        elif 'open linkedin' in query:
            openWebsite("linkedin")

        elif 'open github' in query:
            openWebsite("github")

        elif 'open facebook' in query:
            openWebsite("facebook")

        elif 'play music' in query:
            music_dir = 'D:\\Downloads\\Video'  # Change this to your actual music directory
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found in the specified directory.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\OM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Sir! Have a nice day.")
            break

        else:
            speak("I didn't understand that. Can you please repeat?")
