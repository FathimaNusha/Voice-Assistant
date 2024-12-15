# Text to spoken words
import pyttsx3 as p
# Speak to text
import speech_recognition as sr

from selenium_web import *
from youtube import *
from news import *
import randfacts
from jokes import *
from weather import *
import datetime


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

today_date = datetime.datetime.now()
current_hour = today_date.hour

if current_hour <12:
    greet ="good morning"
elif 18 >current_hour>=12 :
    greet =" good afternoon"
else:
    greet ="good night"


# Recognizer instance
r = sr.Recognizer()


speak("Hello sir")
speak(str(greet) )
speak("I am your voice assistant")    
speak("Today is " + today_date.strftime("%A, %B %d, %Y, and the time is %I:%M %p"))
speak("How are you?")

with sr.Microphone() as source:
    # Low threshold for unclear voice
    r.energy_threshold = 2000
    r.adjust_for_ambient_noise(source, 1.2)
    print('Listening...')
    audio = r.listen(source)

    # Convert voice to text using Google API
    text = r.recognize_google(audio)
    print(text)

    if "fine" in text or "good" in text:
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

        elif "play" in text2 and "video" in text2:
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

        elif "joke" in text2:
            speak("sure sir ")
            arr=joke()   
            print(arr[0])
            speak (arr[0])   
            print(arr[1])
            speak (arr[1]) 

        elif "fact" in text2 or "facts" in text2 or "interesting" in text2:
              speak("sure sir")
              fact = randfacts.get_fact()
              print(fact)
              speak ("Did you know that" + fact)

        elif "weather" in text2 or "temperature" in text2:
            speak("sure sir")
            speak("current temperature of colombo is "+ str(temp()) +"and sky is look l" + str(des()))  


        else:
            speak("Sorry, I couldn't understand your command. Please try again.")
