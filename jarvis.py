import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrery 
import requests 

recognizer=sr.Recognizer()
engine = pyttsx3.init('sapi5')



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com") 

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com") 

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrery.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=eab03b228e304bc98d4f467aa55f127d")

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            for article in articles[:5]:
                speak(article["title"])


if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
        r= sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source, timeout=2,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if("jarvis" in word.lower()):
                speak("bolo,  how can i help you")
               

#Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio=r.listen(source, timeout=2,phrase_time_limit=2)
                    command=r.recognize_google(audio)
                   
                    processCommand(command)

    
        except Exception as e:
            print("waiting {0}".format(e))

