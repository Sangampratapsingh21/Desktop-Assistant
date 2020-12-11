import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import sys
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0,1].id)
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty("rate")
# print(rate)
engine.setProperty("rate", 150)

volume = engine.getProperty("volume")
# print("volume is {0}".format(volume))
engine.setProperty("volume", 1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")
    
    else:
        speak("Good Evening!!")

    speak("I am Stella. Please tell me how may I help you!!")

# def sendEmail(to, content):
#     server = smtplib.SMTP_SSL("smtp.gmail.com",587)
#     server.login("sangampratapsingh21012006@gmail.com", "sangam@123" )
#     server.sendmail("sangamsurendrasingh@gmail.com",
#                     "jiyageetasingh21042010@gmail.com",
#                     "geetasurendrasingh@gmail.com",
#                     "sangampratapsingh21012006@gmail.com", to, content)
#     server.quit()

def takeCommand():
    # It takes command from user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    
    try:
        print("Recognizing...")
        speak("I am trying to recognize what is your command")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
        # speak('Next Command')

    except Exception as e:
        # print(e)
        print("Sorry I didn't get that can you please write your query!")
        speak("Sorry I didn't get this can you please write your query!")
        query = str(input('Command: '))

        #return "None"
    return query

    

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
        
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        # elif 'open youtube' in query:
        #     webbrowser.open("youtube.com")
        
        # elif 'open google' in query:
        #     webbrowser.open("google.com")

        # elif 'open gmail' in query:
        #     webbrowser.open("mail.google.com")
        

        elif 'open youtube' in query:
            speak('OK!Opening...')
            print("OK!Opening...")
            webbrowser.open('www.youtube.com')
            time.sleep(5)

        elif 'open google' in query:
            speak('OK!Opening...')
            print("OK!Opening...")
            webbrowser.open('www.google.com')
            time.sleep(5)

        elif 'open gmail' in query:
            speak('OK!Opening...')
            print("OK!Opening...")
            webbrowser.open('www.gmail.com')
            time.sleep(5)

        elif 'open whatsapp web' in query:
            webbrowser.open('https://web.whatsapp.com ')
            speak('OK!Opening...')
            print("OK!Opening...")
            time.sleep(5) 

        elif 'open stackoverflow'in query or 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")
            print("OK Openining...")
            speak('OK!Opening...')
            time.sleep(5)

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak('OK!Opening...')
            print("OK Openining...")  
            time.sleep(5)

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak('OK!Opening...')
            print("OK Openining...")      
            time.sleep(5)

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak('OK!Opening...')
            print("OK Openining...") 
            time.sleep(5)

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.in")
            speak('OK!Opening...')
            print("OK Openining...")
            time.sleep(5)

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak('OK!Opening...')
            print("OK Openining...") 
            time.sleep(5)

        elif 'play music' in query:
            music_dir= 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            time.sleep(5)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is: {strTime}")

        elif 'news' in query:
            webbrowser.open_new_tab('https://timesofindia.indiatimes.com/home/headlines')
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
            
        elif 'search'  in query:
            search = query.replace("search", "")
            g_url="https://www.google.com/search?q="    
            print("Searching for you on google...")
            speak("Searching for you on google")
            webbrowser.open(g_url+search) 
            time.sleep(5)

# Program opening code
        elif 'open code' in query:
            var1 = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("OK!Opening...")
            speak('OK!Opening...')
            os.startfile(var1)
            time.sleep(5)

        elif 'open firefox' in query:
            var2 = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            print("OK! Opening...")
            speak('OK!Opening...')
            os.startfile(var2)
            time.sleep(5)

        elif 'open chrome' in query:
            var3 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            print("OK! Opening...")
            speak('OK!Opening...')
            os.startfile(var3)
            time.sleep(5)

        elif 'open microsoft edge' in query:
            var4 = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            print("OK! Opening...")
            speak('OK!Opening...')
            os.startfile(var4)
            time.sleep(5)

        elif 'open obs studio' in query:
            var5 = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            print("OK! Opening...")
            speak('OK!Opening...')
            os.startfile(var5)
            time.sleep(5)

        elif 'open word' in query:
            var6 = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.exe"
            print("OK!Opening...")
            speak('OK!Opening...')
            os.startfile(var6)
            time.sleep(5)

        elif 'open excel' in query:
            var6 = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\EXCEL.exe"
            print("OK!Opening...")
            speak('OK!Opening...')
            os.startfile(var6)
            time.sleep(5)

        elif 'open whatsapp' in query:
            var6 = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            print("OK!Opening...")
            speak('OK!Opening...')
            os.startfile(var6)
            time.sleep(5)

        elif 'open powerpoint' in query:
            var7 = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\POWERPNT.exe"
            print("OK!Opening...")
            speak('OK!Opening...')
            os.startfile(var7)
            time.sleep(5)

        elif 'open telegram' in query:
            var8 = "C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            print("OK!Opening...")
            speak('OK!Opening...')
            os.startfile(var8)
            time.sleep(5)

        elif 'nothing' in query or 'abort' in query or 'exit'in query or 'stop' in query:
            speak('okay')
            speak('Bye Master, have a good day.')
            sys.exit()
        
        # else:
        #     temp = query.replace(' ','+')
        #     g_url="https://www.google.com/search?q="    
        #     res_g = 'Sorry! I Cannot understand but I can search from internet to give your answer ! okay'
        #     print(res_g)
        #     speak(res_g)
        #     webbrowser.open(g_url+temp) 

        speak('Next Command please!')
