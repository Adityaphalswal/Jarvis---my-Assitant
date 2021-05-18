import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)
#print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12: #morning Time
        speak("Good Morning, Addu")

    elif hour>=12 and hour<=18: #Good Morning
        speak("Good Afternoon, Addu")
    
    else:
        speak("Good evening, Addu")
    speak("I am Jarvis. How may I help you.")

def takeCommand():
    '''It takes microphone input from user and return srting output'''

    r = sr.Recognizer()
    with sr.Microphone() as  source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f'Addu said:{query}\n')

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()#put password in txt file then read it
    server.login("Myemail@gmail.com", "YourPassword")
    server.sendmail("Myemail@gmail.com", to , content)
    server.close()


if __name__=="__main__":
    #speak("Addu is good boy and he likes to code.")
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open stackover' in query:
            webbrowser.open("stackoverflow.com")
        

        elif 'play music' in query:
            music_dir='C:\\Users\\INTEL\\Desktop\\College Application\\muskan'
            songs = os.listdir(music_dir)
            print(songs) # Use Random module
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strtime}')
        
        elif 'open code' in query:
            codePath = "C:\\Users\\INTEL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open Chrome' in query:
            ChromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(ChromePath)

        elif 'open Git' in query:
            GitPath = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(GitPath)

        elif 'open Prime music' in query:
            codePath = ""
            os.startfile(codePath)

        elif 'open cmd' in query:
            CmdPath = "%windir%\\system32\\cmd.exe"
            os.startfile(CmdPath)
        
        elif 'open python' in query:
            PythonPath = "C:\\Users\\INTEL\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
            os.startfile(PythonPath)
        
        elif 'open Control Panel' in query:
            CPPath = "C:\\Users\\INTEL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel"
            os.startfile(CPPath)
        
        elif 'open Run' in query:
            RunPath = "C:\\Users\\INTEL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run"
            os.startfile(RunPath)
        
        elif 'open Pc' in query:
            ThisPcPath = "C:\\Users\\INTEL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\This PC"
            os.startfile(ThisPcPath)
        
        elif 'open File ' in query:
            FLPath = "C:\\Users\\INTEL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\ File Explorer"
            os.startfile(FLPath)
        
        elif 'open Calculator ' in query:
            CalculatorPath = "C:\\Users\\INTEL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\ File Explorer"
            os.startfile(CalculatorPath)

        #make dictionary
        elif 'email to addu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adityaph135@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Addu, I not able to send this email")


          
