from concurrent.futures import process
import pyttsx3
import datetime
from datetime import date
import  speech_recognition as sr
import wikipedia
from googlesearch import search
import webbrowser
import os
import wolframalpha
import pyjokes
import pywhatkit as pwt
import time
import os
from dotenv import load_dotenv

load_dotenv()




#landing page
print('''=====Welcome to Desktop Assistant=====\n
        Key features:\n
        1. Fun with assistant                                
           Command: who are you,tell me a joke,are you single etc.

        2. Ask about time and date

        3. Anything search on internet                       
           Command: say 'search' and then ask anything such as play 'song' on youtube

        4. Calculation in Mathematics                        
           Command: say calculate 'your question' such as calculate sin30

        5. Send any message on WhatsApp on any given number  
           Command: say send a message

        6. Search anything on wikipedia
           Command: say 'wikipedia'

        7. Find the location on map
           Command: say 'find location'

        6. To exit the programm say 'bye' ''')

#Function to make computer speak
def speak(txt):
    engine = pyttsx3.init('sapi5')
    engine.say(txt)
    engine.runAndWait()

#Function for greeting
def greet():
    hours = int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak("Good Morning Sir")
    elif hours>=12 and hours<18:
        speak("Good Afternoon Sir")
    elif  hours>=18:
        speak("Good evening Sir")
    speak("I am your assistant, tell me How may I help you sir?")



#Function to take command
def take_command(ask = False):
    if ask:
        speak(ask)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        MyText = r.recognize_google(audio, language="en-in")
        MyText = MyText.lower()
        print("User said:"+ MyText)
                
    except:
        speak("I am sorry sir I cant hear you...")
        return 'none'
        
    return MyText


#Function to calculate anything in maths
def calculate():
    try:
        app_id=os.environ.get('APP_ID')

        client = wolframalpha.Client(app_id)
        res = client.query(command)
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)
    except:
        speak("I cant find any result sir")

def SendMsg():
    speak('Enter the number with country code')
    num = input('''Enter the number with country code\n''')
    msg = take_command("What you want to say sir?")
    pwt.sendwhatmsg_instantly(num,msg,20,True,15)
    
if __name__ == "__main__":        
#All the task
    greet()
    while True:
        command=take_command().lower()

        if "wikipedia" in str(command):
            wiki = take_command('What do you want to know on wikipedia sir?')
            speak("Searching wikipedia about" + wiki)
            result = wikipedia.summary(wiki,sentences = 3)
            print(result)
            speak("According to wikipedia")
            speak(result)
            speak('Tell me What can I more sir?')
            

        elif  "bye" in str(command):
            speak("Ok bye sir take care and have a good day")
            break

        elif "who are you" in str(command):
            speak("I am a computer assistant sir. I have been created by Mr Junaid")

        elif str(command) == "thank you":
            speak("Its my pleasure sir.")

        elif "joke" in str(command):
            joke = pyjokes.get_joke(category='neutral')
            print(joke)
            speak(joke)
            speak('Tell me What can I do more sir?')

        elif "are you single" in str(command):
            speak("No sir, I am in relationship with this system")

        elif "time" in str(command):
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            print(time_now)
            speak(f"The time is {time_now}")
            speak('Tell me What can I do more sir?')

        elif "date" in str(command):
            date_today = date.today()
            print(date_today)
            speak(date_today)
            speak('Tell me What can I do more sir?')

        elif "open word" in str(command):
            speak("Opening Microsoft Word")
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD')
            break

        elif "open powerpoint" in str(command):
            speak("Opening Microsoft PowerPoint")
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT')
            break
            
        elif "open excel" in str(command):
            speak("Opening Microsoft Excel")
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL')
            break
            
        elif "open calculator" in str(command):
            speak("Opening Calculator")
            os.startfile('C:\\Windows\\system32\\calc')
            break


        elif "calculate" in str(command): 
            calculate()
            speak('Tell me What can I do more sir?')

        elif "send" in str(command):
            SendMsg()
            break
            

        
        elif 'search' in str(command):
            search_internet = take_command('what do u want to search?')
            if search_internet == 'none':
                speak("I can't hear properly sir!")
                
            else:
                for i in search(search_internet, num_results=1):
                    webbrowser.open_new_tab(i)
                break

            
        elif 'find location' in str(command) or 'find the location' in str(command):
            location = take_command("What is the location sir?")
            if location == "none":
                speak("I can't hear properly sir!")

            else:
                url = 'https://google.nl/maps/place/' + location + '/&amp;'
                webbrowser.get().open(url)
                speak('Here is the location of' + location)
                time.sleep(10)
                speak('Tell me What can I do more sir?')
                


            


        else:
            speak("Say something more appropriate sir")
        


