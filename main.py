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

def main():
  while(True):
      audio=sr.Recognizer()
      engine=pyttsx3.init()
      try:
          with sr.Microphone() as source:
              engine.say("Please say 1 if you wish to continue or say 0 to stop")
              engine.runAndWait()
              voice=audio.listen(source)
              command=audio.recognize_google(voice)
              print(command)
              if(command=='1'):
                  start()
                  actions()
              elif(command=='0'):
                  engine.say("Have a nice day,thank you")
                  engine.runAndWait()
                  break;

      except:
          pass
if __name__=="__main__":
    main()
