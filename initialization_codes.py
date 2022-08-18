import speech_recognition as sr
import pyttsx3
import pywhatkit as wk
import python_weather as pw
import datetime as dt
import asyncio
import os
import sys
import time
import wikipedia
import requests
from bs4 import BeautifulSoup
import pyjokes
print(sys.version)


def start():   
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    #engine.say("Namaste I am Biltu what can I do for you")
    greet()
    engine.runAndWait()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    
    
def listen():
    audio=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Say Something:")
            voice=audio.listen(source)
            command=audio.recognize_google(voice)
            print(command)
    except:
        pass
    return command
  
  
def actions():
    cmd=listen()
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    if 'what can you do' in cmd:
        engine.say('I can play music,give you weather updates,send whatsapp messages,tell you jokes,date and time,current news, do google and wikipedia search')
        engine.runAndWait()
    elif 'weather' in cmd:
        engine.say('Which City weather you want')
        engine.runAndWait()
        audio=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Say Something:")
                voice=audio.listen(source)
                city=audio.recognize_google(voice)
                print(city)
                city = city+" weather"
                weather(city)
        except:
            pass
    elif 'play' in cmd:
        engine.say("playing on youtube")
        engine.runAndWait()
        cmd=cmd.replace('play','')
        wk.playonyt(cmd)
   
    elif ('date' in cmd) or ('todays date' in cmd):
        x=dt.datetime.now()
        engine.say(x.strftime("%c"))
        engine.runAndWait()
    elif 'time' in cmd:
        print('times')
        times()
    elif 'who is' or 'what is' in cmd:
        person=cmd.replace('who is','')
        things=cmd.replace('what is','')
        engine.say(wiki(cmd))
        engine.runAndWait()
    elif 'news' in cmd:
        engine.say(news())
        engine.runAndWait()
    elif 'WhatsApp' in cmd:
        whatsapp()
    elif 'search' in cmd:
        google_search()
    elif 'tell jokes' in cmd:
        engine.say(jokes())
        engine.runAndWait()
    else:
        engine.say("Sorry I don't understand that:")
        engine.runAndWait()
        
