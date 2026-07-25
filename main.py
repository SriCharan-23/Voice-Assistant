'''
Docstring for main
Here is a small project of Voice assistance where we can give commands to our PC for the things we need
It collects the audio given by us and processes it to give us required outputs

Note: It is still has a limited access in future it may be enhanced!!
'''

# These are the modules which are required by us to go on with this project

import speech_recognition as sr #as keyword makes us use 'sr' instead of writing whole word 'speech recognition'
import webbrowser
import pyttsx3    #It is a module used to convert text to speech
import musiclibrary #It is a user defined module
import os
from dotenv import load_dotenv
from google import genai
import re

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

#recognizer class 
recognizer =  sr.Recognizer() 

#This function is used under pyttsx
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def ask_gemini(question):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=question
    )
    return response.text

def clean_text(text):
    text = re.sub(r'#+\s*', '', text)        # remove ### headers
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # remove **bold**
    text = re.sub(r'\*(.*?)\*', r'\1', text)      # remove *italic*
    text = re.sub(r'`(.*?)`', r'\1', text)        # remove `code`
    text = re.sub(r'-\s+', '', text)              # remove leading dashes/bullets
    return text
# This function describes about the processes
def processcommand(c):
    #opens google
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
     #opens instagram 
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
     #opens facebook
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
     #opens youtube  
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
     #opens linkedin  
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
     #opens required song 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        # c.lower().split(" ")[1] -> here we will understand it line by line
        # c.lower()-> even if the key is in capital letters it will convert it to small letters
        #split(" ")-> split function splits 'play' and "song" by a space and stores them as ["play" "song"]
        #[1] -> as before song is stored as ['play' "song"] the index of play is 0 and song is 1, when we keep [1]
        # it stores the 1 index element in the song i.e., the song which we need!!
        link = musiclibrary.Music[song]
        webbrowser.open(link)

    else:
        answer = ask_gemini(c)
        answer = clean_text(answer)
        print("Astra:", answer)
        speak(answer)

if __name__ == "__main__": #generally this condition holds true only if the code is being executed in the same file.
    #function speak() is called here 
    speak(".....rank Initializing Astra")
    try:
        while True:
    
            #Recognize wakeup word "Astra" and wakeup while listening to the correct word
            r= sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=4)
            word = r.recognize_google(audio)
            if "astra" in word.lower():
                
                speak(".....rank Yeah! Iam listening")

                print("Heared:",word)
                with sr.Microphone() as source:
                    #Microphone is also a class which collects audio from microphone
                    print("Astra Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                processcommand(command)



    except Exception as e:
        print("Error {0};".format(e))

