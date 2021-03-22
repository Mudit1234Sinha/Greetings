import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date_1 = int(datetime.datetime.now().day)
    speak(year)
    speak(month)
    speak(date_1)

def wiki():
    speak("What do you want to search ")
    speak("Please enter your search in the below terminal")
    search = input("Enter your search below\n")
    results = wikipedia.summary(search, sentences=3)
    speak("According to wikipedia")
    print(results)
    speak(results)


def wish_me():
    speak("Welcome back sir! ")
    speak("The current time is ")
    time()
    speak("The current date is")
    date()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    elif 18 <= hour < 24:
        speak("Good evening sir")
    else:
        speak("Good Night sir")
    speak("Jarvis at your service.Please tell me how can i help you")
    wiki()

wish_me()





