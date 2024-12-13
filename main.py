# Text to spoken words
import pyttsx3 as p
# Speak to text
import speech_recognition as sr

from selenium_web import *
from youtube import *
from news import *
import randfacts


# Instance of pyttsx3
engine = p.init()

# Set voice speed
engine.setProperty('rate', 130)

# Available voices
voices = engine.getProperty('voices')

# Set voice as female
engine.setProperty('voice', voices[1].id)

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Recognizer instance
r = sr.Recognizer()

speak("Hello sir, I am your voice assistant. How are you?")

with sr.Microphone() as source:
    # Low threshold for unclear voice
    r.energy_threshold = 2000
    r.adjust_for_ambient_noise(source, 1.2)
    print('Listening...')
    audio = r.listen(source)

    # Convert voice to text using Google API
    text = r.recognize_google(audio)
    print(text)

    if "what" in text and "about" in text and "you" in text:
        speak("I am also having a good day, sir.")
    speak("What can I do for you?")

    with sr.Microphone() as source:
        r.energy_threshold = 2000
        r.adjust_for_ambient_noise(source, 1.2)
        print('Listening...')
        audio = r.listen(source)

        text2 = r.recognize_google(audio)
        print(text2)

        if "information" in text2:
            speak("sure sir, Which topic related information do you want?")
            with sr.Microphone() as source:
                r.energy_threshold = 2000
                r.adjust_for_ambient_noise(source, 1.2)
                print('Listening...')
                audio = r.listen(source)

                text3 = r.recognize_google(audio)
                print(text3)

                speak(f"Searching {text3} in Wikipedia.")
            assist = infow()
            assist.get_info(text3)

        elif "play" and "video" in text2:
            speak("sure sir , Which video do you want to play?")
            with sr.Microphone() as source:
                r.energy_threshold = 2000
                r.adjust_for_ambient_noise(source, 1.2)
                print('Listening...')
                audio = r.listen(source)

                text4 = r.recognize_google(audio)
                print(text4)

                speak(f"Playing {text4} on YouTube.")
            assist = music()
            assist.play(text4)

        elif "news" in text2:
            print("sure sir, now i will read recent news for you")
            arr=news()   
            for news_item in arr:
              print(news_item)
              speak (news_item)

        elif "fact" or "facts" or "interesting" in text2:
              speak("sure sir")
              fact = randfacts.getFact()
              print(fact)
              speak ("Did you know that" + fact)
        

        else:
            speak("Sorry, I couldn't understand your command. Please try again.")
