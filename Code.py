import pyttsx3
import datetime
import wikipedia
import speech_recognition as spch
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hr=int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good morning")
    elif hr>=12 and hr<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis, how can i help you sir")
def forCommand():
    #this function will take microphone input from the user and is going to retrurn it as string output
    r=spch.Recognizer()
    with spch.Microphone() as source:
        print("I am listening.....")
        r.energy_threshold=600
        audio=r.listen(source)

    try:
        print("Recognizing")
        query= r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "NONE"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email here',"your password here")
    server.sendmail('youremailhere',to,content)
    server.close()

if __name__=='__main__':
    # speak("i am noob")
    wishme()
    
    while True:
        query=forCommand().lower()
        #executing tasks based on query
        if "wikipedia" in query:
            speak("Searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open my favourite youtube channel" in query:
            webbrowser.open("https://www.youtube.com/channel/UC7Q7pl0z0MrdayvmAnchlJQ")
        elif "open google" in query:
            webbrowser.open("www.google.com")
        elif "open my college site" in query:
            webbrowser.open("http://vlearn.veltech.edu.in/login/index.php")
        elif "play music" in query:
            song_dir='D:\\Program Files\\song'
            songs=os.listdir(song_dir)
            c=len(songs)-1
            i=random.randint(0,c)
            os.startfile(os.path.join(song_dir,songs[i]))
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
        elif "open code" in query:
            pathc="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.4\\bin\\pycharm64.exe"
            os.startfile(pathc)
        elif 'email to me' in query:
            try:
                speak("what should i say")
                content=forCommand()
                to='destinationemialhere'
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Failed to send")
                print("Failed!!")
        elif "turn off" in query:
            exit()
