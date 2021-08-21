import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Dharmendra")
    elif hour>12 and hour<=18:
        speak("Good evening Dharmendra")
    else:
        speak("Good night Dharmendra")
    speak("I am Jaarvis Mam..a project by your students How can I help you")
    
    speak("Maam I am jarvis, speed 1 giga hertz and memory 1 tera byte")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
 
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("dharmendrakumarsah133@gmail.com",'opengmail123')
    server.sendmail('dharmendrakumarsah133@gmail.com',to,content)
    server.close()
if __name__=="__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'who are you' in query:
            speak("Dear mam, I am Jarvis a project of data structure and algorithm made by your obedient students Dharmendra kumar sah 19BCE2633 and ABHISHEK KANDEL 19BCE2629")3W2`    z
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'who is you ' in query:
            speak("I am Jar vis mam, a project made by your students")
        elif 'tell me about yourself' in query:
            speak('mam this is jar vis a project made by your students')
        elif 'give me your details' in query:
            speak('sorry maam,  my owner did not allowed me tell confidential information, yaa of course you can ask me for some other help')
        elif 'send email to ram' in query:
            try:
                speak("What shoud I say")
                content=takeCommand()
                to="dharmendrakumarsah133@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent, you can check now")
            except Exception as e:
                print(e)
                speak("Sorry Mam, I am not able to send email, I think there is some mistake could you please check out that once.. and try again")
        elif 'exit' in query:
            exit()
                
    