import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning sahil,what a lovely day,how may i help you')
    elif hour >= 12 and hour < 16:
        speak('good afternoon sahil,how may i help you')
    elif hour >= 16 and hour < 24:
        speak('good evening sahil,how may i help you')

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('please tell me your request, i am listening..')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print('user said: {}\n'.format(query))
        except Exception as e:
            #print(e)

            print("I was unable to understand what you just said. Could you please repeat your command..")
            return "None"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail@gmail.com','your password')
    server.sendmail('yourgmail@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
    #logic to execute task based on query

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print('Time:{}'.format(strTime))
            speak('The time is:{}\n'.format(strTime))

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\91886\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to sahil' in query:
            try:
                speak('what should i say?')
                content = takeCommand()
                to = 'emailid@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent.')
            except Exception as e:
                speak("Sorry, the email hasn't been sent at the moment")