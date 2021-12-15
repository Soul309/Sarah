import speech_recognition as sr
import wikipedia
import os
import pyttsx3
import datetime
import webbrowser
import requests
import time

#Virtual Desktop assistant made by Gaurav


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("morning sir i am sara created by Gaurav how may i help you")
    elif hour <=12 and hour<18:
        speak("good afternoon sir i am sara created by Gaurav how may i help you")
    else:
        speak("good evening sir i am sara created by Gaurav how may i help you ")


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        print("recognizing")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:
        print("conection error")
        return "none"
    return text


if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()


        if "wikipedia" in query:
            speak("wait sir i am searching")
            #query.replace("wikipedia" +)
            results = wikipedia.summary(query ,sentences=2)
            print(results)
            speak(results)
        
        elif "google" in query:
            speak("opening google sir")
            webbrowser.open("www.google.com")
        
        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")
        
        elif "play music"  in query:
            speak("opening music sir")
            music_dir ="./music"
            music = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,music[0]))
        
        elif "goodbye" in query:
            speak("ok bye sir")
            exit()
        
        elif "open instagram" in query:
            speak("ok sir ")
            webbrowser.open("www.instagram.com")
        
        elif "open gmail" in query:
            speak("opening gmail sir")
            webbrowser.open("www.gmail.com")
        
        elif "who created you" in query:
            speak("i have been created by Gaurav")
        
        elif "what is your name" in query:
            speak("my name is sara")
        
        elif "open virtualbox" in query:
            speak("ok sir opening virtualbox...")
            apps_dir ="C:\Program Files\Oracle\VirtualBox"
            apps = os.listdir(apps_dir)
            os.startfile(os.path.join(apps_dir , apps[60]))
            time.sleep(5)
        
        
        elif "shutdown" in query:
            speak("ok sir shutting down the pc bye")
            os.system("shutdown /s /t 1")
        
       
        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takecom()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
        
       
        
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        
        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open(query)
            time.sleep(3)
        
        
        elif 'linkedin' in query:
            speak("ok sir opening linkedin")
            webbrowser.open("https://www.linkedin.com/in/gaurav-mishra-5090a519b/")
        
        
        elif 'who are you' in query or "what can u do" in query or "introduce yourself" in query:
            speak("I am a virtual desktop assistant sarah made in python language by Gaurav. I am programmed to do so many tasks like 'opening youtube, google chrome, gmail and linkedin ,predict time,playing music,search wikipedia, predict weather" 
                  "in different cities , can search anything on google ,  get top headline news from times of india and can shutdown whole system too")
        
        elif "open my college website" in query or "college" in query:
            speak("ok sir  opening your college website")
            webbrowser.open("https://www.gbu.ac.in/")
            time.sleep(4)