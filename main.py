import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
import random
import subprocess
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('raza.uwais21@vit.edu', 'owaisraza9075')
    server.sendmail('raza.uwais21@vit.edu', to, content)
    server.close()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis, Your virtual assistance")
    speak("Tell me How can I help you")
def TakeCommand():
    """it takes speech input from user and returns string output"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in').lower()
        print(f"User said: {query}\n")
    except Exception as e:
        print("Did not recognize, say that again please")
        speak('did not recognize, say that again sir')
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query=TakeCommand().lower()
        try:
            if 'wikipedia' in query:
                print("searching wikipedia....")
                speak('searching wikipedia....')
                query=query.replace('wikipedia', '')
                results=wikipedia.summary(query ,sentences=2)
                speak('according to wikipedia')
                print(results)

                speak(results)
        except Exception as e:
            print("Data not found")
            speak('data not found')
        if 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'play music' in query:
            music_dir='C:\\music_dir'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,3)]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f'sir, the time is {strTime}')

        elif 'today date' in query:
            strTime1= datetime.date.today()

            speak(f'sir, todays date is {strTime1}')
        elif 'send email' in query:
            try:
                speak('what should I say, sir')
                content=TakeCommand()
                to='owaisraza7297@gmail.com'
                sendEmail(to, content)
                print('Email has sent')
                speak('email has sent')
            except Exception as e:
                speak('sorry sir,I am facing problem in sending this email.')


