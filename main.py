
import webbrowser
import speech_recognition as sr
import os
import datetime
import random
import pyttsx3
import wikipedia
greeting = ['hey there', 'hello', 'hi', 'Hai', 'gandu', 'hey']
grres = ["hey Rushikesh ", 'hello whatsap ']
question = ['hello how are you', 'What are you doing', "what's your mind"]
boar = ['i am getting boar', 'tell me something', 'boar', "bored", ]
entertane = ["lets do something", 'don\'t worry', 'I am here']
responses = ['I am doing well hope you and your loved onces are safe in this time', "I'm fine"]
ytcmd = ['open youtube', 'i want to watch a video']
favsong = ['play my song', 'play tera fitur', 'song']
rep = ['repeat', 'copy me', 'repeat me', 'say with me']
back = ['exit', 'close', 'goodbye', 'nothing', 'bye']
clr = ["clear my screen","clear","clean"]
gaali = ["haramkhor",'lavde','chutiya','gandu','madarchod']
language = 'en'
sentence = "Hey, say something."
sound=[1,2,0]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
i =0
engine.setProperty('voice', voices[0].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        print("Good Morning")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")  
        print(("Good Afternoon!")) 

    else:
          
        print("Good Evening!")
        speak("Good Evening!")
    print("I am space sir ,Please tell me how may I help you?")
    speak("I am space sir , Please tell me how may I help you")  

def clear():
    os.system("cls")

def repeat(bol):
    
    re = listen()
    speak(re)

    return re


def website(webname):
    print("opening" + " " + "link" + "(" + webname+")..")
    webname = "www."+webname+".com"
    webbrowser.open(webname, new=2)
    

def open(link):
    print("Opening your favorite song...")
    webbrowser.open(link, new=2)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def speak(say):

#     language = "en"
#     obj = gTTS(text=say, lang=language, slow=False)
#     obj.save("sound.mp3")
#     playsound("sound.mp3")
#     os.remove("sound.mp3")


def listen():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
       
        try:
         print("Recognizing...")    
         audiosaid = r.recognize_google(audio, language='en-in')
         print(f"you said =) {audiosaid}\n")
        except Exception as e:
         
         print("Say that again please...")  
         return "None"
  
    return audiosaid        
   




clear()
name = "Rushikesh"
wishMe()
# print('hey\' welcome can I know your name ')
# speak("can I know your name sir ")
# name = listen()
# print("hello"+name)    
# speak("Hey"+name)

while True:
    
    
    voice = listen().lower()
    if voice in greeting:
        greet = random.choice(grres)
        print(greet)
        speak(greet)
    elif voice in favsong:
        song = "https://www.youtube.com/watch?v=qfdShSZZxlg&ab_channel=TipsOfficial"
        speak("playing your favorie song on youtube")
        open(song)

    elif voice in question:
        reply = random.choice(responses)
        print(reply)
        speak(reply)
    elif voice in boar:
        reply1 = random.choice(entertane)
        speak(reply1)
        print(reply1)
    elif voice in back:
        ba = random.choice(back)
        speak(ba)
        print("okk sure")
        print("..... have a nice day......")
        speak("ok Have a nice day see you ")
        break
    elif voice in clr:
        speak("ok sure cleaning your screen")
        clear()
    elif voice in gaali:
        gali = random.choice(gaali)
        speak(gali)
    elif voice in rep:
     bol = "sure , just tell me what ?"
     speak(bol)
     said = listen()
     while(said!="close"): 
      speak(said)
      said=listen()
      
   
    
        # Logic for executing tasks based on query
    elif 'wikipedia' in voice:
            speak('Searching Wikipedia...')
            voice = voice.replace("wikipedia", "")
            results = wikipedia.summary(voice, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
    elif voice == "open code":
        path = 'C:\\Users\\Rushikesh Chopade\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(path)
    
    elif 'change' in voice:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        j = random.choice(sound)
        engine.setProperty('voice', voices[1].id)
        msg='sure'+" "+name +" "+'I have changed my voice for you , is it prettier ?'
        print(msg)
        speak(msg)
       
        conform = listen()

        if 'no' in conform:
            
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')
                
                engine.setProperty('voice', voices[2].id)
                msg='sure'+" "+name +" "+'I have changed my voice for you , is it prettier ?'
                print(msg)
                speak(msg)
        if 'try other' in conform:
            line = "ok, sound is setted to default"
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
                
            engine.setProperty('voice', voices[0].id)
            msg='sure'+" "+name +" "+'I have changed my voice for you , is it prettier ?'
            print(line)
            speak(line)

        else :
                print("ok I will use this voice from now")    
                speak(("ok I will use this voice from now") )
                
    elif 'the time' in voice:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
    elif 'open google' in voice:
        website("google")
        speak("opening google")
    elif 'open youtube' in voice:
        website('youtube')
        speak("opennning youtube")
    elif 'open spotify' in voice:
        path1 = "C:\\Users\\Rushikesh Chopade\\Desktop\\Spotify.lnk"
        os.startfile(path1)
    elif 'open WhatsApp' in voice:
        path2="C:\\Users\\Rushikesh Chopade\\Desktop\\WhatsApp.lnk"
        os.startfile(path2)
        speak("openning WhatsApp")
        break
    