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


def times():
    x=dt.datetime.now()
    engine=pyttsx3.init()
    print(x.strftime("%I")+":"+x.strftime("%M")+" "+x.strftime("%p"))
    engine.say(x.strftime("%I")+":"+x.strftime("%M")+" "+x.strftime("%p"))
    engine.runAndWait()
    #print(x.strftime("%H")+":"+x.strftime("%M")+" "+x.strftime("%p"))
    
def greet():
    x=dt.datetime.now()
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    #print(x.strftime("%H"))
    y=int(x.strftime("%H"))
    if(y>=5 and y<12):
        engine.say("Good morning How can I help you")
        engine.runAndWait()
    elif(y>=12 and y<16):
        engine.say("Good afternoon How can I help you")
        engine.runAndWait()
    else:
        engine.say("Good evening How can I help you")
        engine.runAndWait()

        
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    engine=pyttsx3.init()
    engine.say(location)
    engine.say(time)
    engine.say(info)
    engine.say(weather+"°C")
    engine.runAndWait()
    print(location)
    print(time)
    print(info)
    print(weather+"°C")
    
 
def wiki(cmd):
    result = wikipedia.summary(cmd,4)
    engine=pyttsx3.init()
    engine.say(result)
    print(result)
    

def whatsapp():
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("Please type the number you want to send message: ")
    engine.runAndWait()
    number=input("Type the number:")
    engine.say("Please say the message you want to send : ")
    engine.runAndWait()
    audio=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Say Something:")
            voice=audio.listen(source)
            message=audio.recognize_google(voice)
            print(message)
            engine.say("Sending...")
            engine.runAndWait()
            wk.sendwhatmsg_instantly(f"+91{number}",message)
    except:
        pass
      

engine=pyttsx3.init()
def news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['BBC World News TV', 'BBC World Service Radio',
                'News daily newsletter', 'Mobile app', 'Get in touch']

    for x in list(dict.fromkeys(headlines)):
        if x.text.strip() not in unwanted:
            engine.say(x.text.strip())
            engine.runAndWait()
            
            
def jokes():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

  
  def google_search():
    audio=sr.Recognizer()
    engine=pyttsx3.init()
    try:
        with sr.Microphone() as source:
            engine.say("Tell Search topic:")
            engine.runAndWait()
            voice=audio.listen(source)
            command=audio.recognize_google(voice)
            print(command)
            wk.search(command)
    except:
        pass
