import speech_recognition as sr
import os
import pyttsx3
import random
import time
import datetime


names = ["sid", "nargis"] 
usrname = random.choice(names) 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",180)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning, hello everuone!")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon, hello everyone !")  
    else:
        speak("Good Evening, hello everyone!") 

    speak("My self jarvis.")

def add_usr(name):
    speak("who are you?!!")
    print("who are you?!!")
    takeCommand()
    time.sleep(1)
    names.append(name)
    speak("now you can access me")
    print("now you can access me")
    speak("i have added your name in user list")   
    print("i have added your name in user list") 

def guess (): # Can you guess to whom u are talking
    speak("Sure!!!, Just a minute")
    speak(f"I think you are " + usrname)
    print("I think you are " + usrname)
    time.sleep(1)
    speak(f"can you tell me {usrname} where i am ? ")
    print(f"can you tell me {usrname} where i am ? ")
    destination = takeCommand()
    main_word = destination.replace("you are in ", "") # you have to say only Place name
    print(main_word)
    time.sleep(0.5)
    speak(f"""Wait for a minute.
    I am searching about {main_word}. 
    And then You can ask Any question from me. """)
    print(f"""Wait for a minute.
    I am searching about {main_word}. 
    And then You can ask Any question from me. """)  

def hello():
    speak("Right now, too whom i am talking?")
    print("Right now, too whom i am talking?")
    input_name = takeCommand()
    
    if input_name == "guess me":
        return guess()
    else:
        return add_usr(input_name)       

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
     
    r = sr.Recognizer() 
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 100
        audio = r.listen(source)
  
    try: 

        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

if __name__== '__main__':
    hello()
    while True:  

        Wake_up = takeCommand().lower()

        if "wake up" in Wake_up:
            os.startfile("C:\\Users\\dna83\\OneDrive\\Desktop\\pro-karm\\jarvis.py")
        else: 
            print("sorry")