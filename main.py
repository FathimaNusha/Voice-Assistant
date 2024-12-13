#text to spoken words
import pyttsx3 as p
#speak to text
import speech_recognition as sr

#instance of p
engine = p.init()

#voice speed
rate= engine.getProperty('rate')
engine.setProperty('rate',130)

#available voices 
voices = engine.getProperty('voices')
#print(voices)

#set voice as female
engine.setProperty('voice',voices[1].id)


def speak(text):
  engine.say(text)
  engine.runAndWait()


r = sr.Recognizer()

speak("Hello sir i am your voice assistant, How are you")

with sr.Microphone() as source:
    #not clear voice low threshold
    r.energy_threshold = 5000
    r.adjust_for_ambient_noise(source,1.2)
    print('Listening')
    audio= r.listen(source)

    #voice send to google API and convert to text
    text = r.recognize_google(audio)
    print(text)

    if " what" and "about" and "you" in text:
       speak("i am also having a good day sir")
    speak("what can i do for you")

    with sr.Microphone() as source:

        r.energy_threshold = 5000
        r.adjust_for_ambient_noise(source,1.2)
        print('Listening')
        audio= r.listen(source)

        text2 = r.recognize_google(audio)
        print(text2)

    if "information " in text2:
        speak("which topic related informatin you want")
        with sr.Microphone() as source:
          r.energy_threshold = 5000
          r.adjust_for_ambient_noise(source,1.2)
          print('Listening')
          audio= r.listen(source)

          text3 = r.recognize_google(audio)
          print(text3)

        speak("searching {}in wikipedia ".format(text3))  
        assist=infow()
        assist.get_info(text3)
 

