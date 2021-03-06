import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import wallpapers
import aboutkm


regulation = ["it is my duty", "welcome"]  
names = ["sid", "nargis"]      
    

Email={'pooja didi':'poojanagar76@gmail.com','veena didi':'veenachandu@gmail.com','hanish':'hanish.arora8@gmail.com','sid':'dna8377850@gmail.com','nargis':'nannikhan72@gmail.com'}

def checker(key):
    if key in Email:
        return Email[key]
    else:
        return "no user found sorry"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",180)


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

def TaskExecution():
    speak("Hello , I am Jarvis")
    speak("HOw Can i Help you")


    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        
        server.login('your email id', 'your email password')
        server.sendmail('your email id', to, content)
        server.close()

    def news():
        main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=dd99e5301ef942e0a2748194efc4ad40"

        main_page = requests.get(main_url).json()
        articles = main_page["articles"]
        head=[]
        day=["first","second","third"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            speak(f"today's {day[i]} news is: {head[i]}")  
            print(f"today's {day[i]} news is: {head[i]}")


    while True:

         
        query = takeCommand().lower()
         
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
 
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)    
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'what is news' in query:
            speak("today is news is")
            news()     
        
        elif 'send mail to' in query: # you can mail to sid, veena didi,hanish bhaiya, nargis, pooja didi
            try:
                to = query.replace("send mail to ", "")
                speak(f"What should I write to {to}? ")
                content = checker(takeCommand()) 
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email") 


        elif "calculate" in query:
             
            app_id = "Enter Your App id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")    
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query) 

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 

        elif "weather" in query:
            speak("city name:")
            print("city name:")
            CITY = takeCommand()
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            API_KEY = "Enter Your Api Key"
            URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
            response = requests.get(URL)
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = main['temp']
                humidity = main['humidity']
                pressure = main['pressure']
                report = data['weather']
                print(f"{CITY:-^30}")
                speak(f"{CITY:-^30}")
                print(f"Temperature: {temperature}")
                speak(f"Temperature: {temperature}")
                print(f"Humidity: {humidity}")
                speak(f"Humidity: {humidity}")
                print(f"Pressure: {pressure}")
                speak(f"Pressure: {pressure}")
                print(f"Weather Report: {report[0]['description']}")
                speak(f"Weather Report: {report[0]['description']}")
            else:
                print("sorry sir i can't find the weather report")
                speak("sorry sir i can't find the weather report")

                



        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\dna83\\OneDrive\\Desktop\\my nunny\\first_project1"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"ma, the time is {strTime}")

        elif 'open command prompt' in query:
            apath =  "C:\\Users\\dna83\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools" 
            os.system("start cmd")

        elif "write a note" in query:
            speak("What should i write, mam")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("mam, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "user list" in query:
            no_of_users = len(names)
            speak(f"Sir there are {no_of_users} users")
            speak("these are their names")
            print(names)
        
        elif "you need a break" in query:
            speak("Ok Sir, you Can call me anytime")
            speak("Just say Wake jarvis!!")
            break  

 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, mam")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change name" in query:
            speak("What would you like to call me, mam ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me jarvis")
            print("My friends call me jarvis")
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I am god gifted for you.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
 
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to nunny. further It's a secret")
 
        elif 'is love' in query:
            speak("It is 9th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by my dear friend sid")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by sid ")

        elif "Thanks" in query or "thank you " in query:
            regu = random.choice(regulation)
            speak(regu)
            print(regu)
          
 
        elif 'change background' in query:
            setwallpaper = random.choice(wallpapers.walpaper)
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                        setwallpaper,
                                                       0)
            speak("Background changed successfully")
        
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"]) 
                     
        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                          
            speak(f" the time is {strTime}")

            webbrowser.open("wikipedia.com")
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "i love you" in query:
            speak("It's hard to understand,I love you a ton and million")


        elif "about Karam Marg" in query or "about karm marg" in query:
            about = aboutkm.aboutKM
            speak(about)
            print(about) 

        elif "video of karam marg" in query:
            speak("wait for a minute") 
            speak("i am searching out the vedio")
            webbrowser.open("https://www.youtube.com/watch?v=i1V6N97h5So")  



TaskExecution()
