import speech_recognition as sr # recognise speech
import playsound # to play an audio files
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import ezgmail
import pywhatkit
import subprocess
import wolframalpha
import requests
import json
import datetime
import pyjokes
import pvporcupine

client = wolframalpha.Client("LVATP4-5RLRA9YLTT")

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def mail():
    voice1 = pyttsx3.init()
    r = sr.Recognizer()
    voice1.say("Sorry you will have to enter the email address manually")
    voice1.say("Enter recipant")
    voice1.runAndWait()
    recipant = voice1
    recipant = voice1("Enter recipant :")
    voice1.runAndWait()
    with sr.Microphone() as source1:
        print("Enter Email Subject :")
        voice1.say("Enter Email Subject")
        voice1.runAndWait()
        audio1 = r.listen(source1)
        try:
            text1 = r.recognize_google(audio1)
            print(f"Subject :{text1}\n")
            subject = text1
            with sr.Microphone() as source2:
                print("Compose Email :")
                voice1.say('compose mail')
                voice1.runAndWait()
                audio2 = r.listen(source2)
                try:
                    text2 = r.recognize_google(audio2)
                    print(f"Text :{text2}\n")
                    text0 = text2

                    ezgmail.send(recipant, subject, text0)


                except:
                    print("Error")
                    voice1.say("error")
                    voice1.runAndWait()
        except:
            print("Error")
            voice1.say("error")
            voice1.runAndWait()

def msg():
    number=int(input("Enter number :"))
    pywhatkit.sendwhatmsg(number, "Test-1", 17, 44)

def calculator():
    subprocess.Popen("C:\Windows\System32\calc.exe")
def cmd():
    subprocess.Popen("C:\Windows\System32\cmd.exe")
def control_panel():
    subprocess.Popen("C:\Windows\System32\control.exe")
def task_manager():
    subprocess.Popen("C:\Windows\System32\Taskmgr.exe")
def paint():
    subprocess.Popen("C:\Windows\System32\mspaint.exe")
def notepad():
    subprocess.Popen("C:\Windows\notepad.exe")
def chess():
    subprocess.Popen("C:\Windows\winsxs\amd64_microsoft-windows-s..iuminboxgames-chess_31bf3856ad364e35_6.1.7600.16385_none_d0c99374981840d5\Chess.exe")
def place():
    subprocess.Popen("C:\Windows\winsxs\amd64_microsoft-windows-s..oxgames-purbleplace_31bf3856ad364e35_6.1.7600.16385_none_622070221822eb39\PurblePlace.exe")
    
    
def news():
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=d0f87943e04649fdb499f9e9e6bc69dc');
    response = requests.get(url).text
    news_dicts=json.loads(response)
    arts=news_dicts['articles']
    
    for articles in arts:
        engine_speak(articles['title'])
        print(articles['title'])
        engine_speak('moving on the next news')

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine_speak('good morning sir')
    elif hour>=12 and hour<18:
        engine_speak('Good afternoon sir')
    else:
        engine_speak('Good evening sir')

def respond(voice_data):
    
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        wishMe()
        greetings = ["vanakam, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
    
    if there_exists(['project details','tell me who developed you','about yourself']):
        engine_speak(" Vanakam, I'm Shayera, I'm a virtual assistant that is designed by team of three members from dhanalakshmi Srinivasan engineering college")
        engine_speak("I will be the next generation virtual assistant that i can assist for various actions")
        engine_speak("team of three members name harrish raj,arun,anand was developed me...")

    if there_exists(['calculator']):
        print("opening Calculator")
        engine_speak("opening Calculator")
        calculator()

    if there_exists(['task manager']):
        print("opening task manager")
        engine_speak("opening task manager")
        task_manager()

    if there_exists(['command prompt']):
        print("opening command prompt")
        engine_speak("opening command prompt")
        cmd()
    
    if there_exists(['notepad']):
        print("opening notepad")
        engine_speak("opening notepad")
        notepad()

    if there_exists(['paint']):
        print("opening paint")
        engine_speak("opening paint")
        paint()

    if there_exists(['chess']):
        print("opening chess")
        engine_speak("opening chess")
        chess()

    if there_exists(['place']):
        print("opening purble place")
        engine_speak("opening purble place")
        place()

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak("my name is Shayera, i'm your personal companinon... ")
        else:
            engine_speak("i dont know my name . what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    if there_exists(["alpha"]):
        engine_speak("start ask me a question")
        print("start ask me a question")
        while True:
            app_id = "LVATP4-5RLRA9YLTT"
            query = record_audio()
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            engine_speak(answer)


    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    #7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
    
    # search for music
    if there_exists(["play music"]):
        search_term= voice_data.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to"+ search_term +"enjoy sir")
    #search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url="https://www.amazon.in/s?k="+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on amazon.com")
         
    #make a note
    if there_exists(["make a note"]):
        search_term=voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes sir")
    elif there_exists(["docs"]):
        search_term=voice_data.split("for")[-1]
        url="https://docs.google.com/"
        webbrowser.get().open(url)
        engine_speak("Here you can make word document sir ")
    elif there_exists(["slides"]):
        search_term=voice_data.split("for")[-1]
        url="https://slides.google.com/"
        webbrowser.get().open(url)
        engine_speak("Here you can make presentation sir")
    elif there_exists(["docs"]):
        search_term=voice_data.split("for")[-1]
        url="https://sheets.google.com/"
        webbrowser.get().open(url)
        engine_speak("Here you can make excel documents sir")
    elif there_exists(["classroom"]):
        search_term=voice_data.split("for")[-1]
        url="https://classroom.google.com"
        webbrowser.get().open(url)
        engine_speak("opening your classroom sir ")
    elif there_exists(["meet"]):
        search_term=voice_data.split("for")[-1]
        url="https://meet.google.com"
        webbrowser.get().open(url)
        engine_speak("here you can create your meetings sir")
    elif there_exists(["classroom"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.classroom.google.com"
        webbrowser.get().open(url)
        engine_speak("opening your classroom sir ")
    elif there_exists(["scholar"]):
        search_term=voice_data.split("for")[-1]
        url="https://scholar.google.com/scholar?as_sdt=2007&q="+search_term
        webbrowser.get().open(url)
        engine_speak("here what i found for"+search_term+"for research papers")
    elif there_exists(["scholar"]):
        search_term=voice_data.split("for")[-1]
        url="https://scholar.google.com/scholar?as_sdt=2007&q="+search_term
        webbrowser.get().open(url)
        engine_speak("here what i found for"+search_term+"for research papers")
    
   
    #open instagram
    if there_exists(["open instagram"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram,sir")
    elif there_exists(["direct messages"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/direct/inbox/"
        webbrowser.get().open(url)
        engine_speak("opening instagram direct messages,sir")
    elif there_exists(["insta profile"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/harrishraj.a/"
        webbrowser.get().open(url)
        engine_speak("opening your instagram profile, sir")
    elif there_exists(["insta search"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"+search_term
        webbrowser.get().open(url)
        engine_speak("here what i found for your keyword"+search_term, "sir")


    #open facebook 

    if there_exists(["open facebook"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/"
        webbrowser.get().open(url)
        engine_speak("opening facebook ,sir")
    elif there_exists(["facebook watch"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/watch"
        webbrowser.get().open(url)
        engine_speak("opening your facebook watch section ,sir")
    elif there_exists(["facebook notifications"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/notifications"
        webbrowser.get().open(url)
        engine_speak("here is your facebook notifications ,sir")
    elif there_exists(["facebook messages"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/messages"
        webbrowser.get().open(url)
        engine_speak("here is your message section of facebook ,sir")
    elif there_exists(["facebook marketplace"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/marketplace/?ref=app_tab"
        webbrowser.get().open(url)
        engine_speak("opening your facebook marketplace section ,sir")
    elif there_exists(["facebook groups"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/groups/feed"
        webbrowser.get().open(url)
        engine_speak("opening your facebook group section ,sir")
    elif there_exists(["facebook groups"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/groups/feed"
        webbrowser.get().open(url)
        engine_speak("opening your facebook group section ,sir")
    elif there_exists(["group notifications"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/groups/notifications"
        webbrowser.get().open(url)
        engine_speak("opening your facebook group notifications ,sir")
    elif there_exists(["facebook gaming"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/gaming/?ref=games_tab"
        webbrowser.get().open(url)
        engine_speak("opening your facebook game section ,sir")
    elif there_exists(["facebook gaming"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/gaming/?ref=games_tab"
        webbrowser.get().open(url)
        engine_speak("opening your facebook game section ,sir")
    elif there_exists(["facebook profile"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/HarrishLethal/"
        webbrowser.get().open(url)
        engine_speak("here is your facebook profile ,sir")
    elif there_exists(["facebook settings"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/settings"
        webbrowser.get().open(url)
        engine_speak("here is your facebook settings ,sir")
    elif there_exists(["facebook settings"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/settings"
        webbrowser.get().open(url)
        engine_speak("here is your facebook settings ,sir")
    elif there_exists(["on fb settings"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/settings?tab="+search_term
        webbrowser.get().open(url)
        engine_speak("here i open the settings ,sir")
    
       
    #open twitter
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")
    elif there_exists(["open twitter home "]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/home"
        webbrowser.get().open(url)
        engine_speak("opening twitter home ")
    elif there_exists(["open twitter explore "]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/explore"
        webbrowser.get().open(url)
        engine_speak("opening twitter explore ")
    elif there_exists(["open twitter notifications "]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/notifications"
        webbrowser.get().open(url)
        engine_speak("opening twitter notifications")
    elif there_exists(["open twitter messages "]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/messages"
        webbrowser.get().open(url)
        engine_speak("opening twitter messages")
    elif there_exists(["open my profile "]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/HarrishRaj33"
        webbrowser.get().open(url)
        engine_speak("showing your profile ")
    elif there_exists(["show my tweets "]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/HarrishRaj33/with_replies"
        webbrowser.get().open(url)
        engine_speak("showing your tweets and replies")
    elif there_exists(["show my media"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/HarrishRaj33/media"
        webbrowser.get().open(url)
        engine_speak("showing your media on twitter")
    elif there_exists(["show my likes "]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/HarrishRaj33/likes"
        webbrowser.get().open(url)
        engine_speak("showing your likes on twitter")
    elif there_exists(["tweet"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/compose/tweet"
        webbrowser.get().open(url)
        engine_speak("here your can tweet on twitter ")
    elif there_exists(["open twitter settings"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/settings/account"
        webbrowser.get().open(url)
        engine_speak("opening twitter settings ")
    elif there_exists(["open twitter home "]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/home"
        webbrowser.get().open(url)
        engine_speak("opening twitter home ")
    elif there_exists(["on twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/search?q="+search_term
        webbrowser.get().open(url)
        engine_speak("here what i found for"+search_term+"on twitter")
    

    if there_exists(["open linkedin"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/"
        webbrowser.get().open(url)
        engine_speak("opening linkedin")
    elif there_exists(["my account"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/in/a-harrish-raj/"
        webbrowser.get().open(url)
        engine_speak("opening your account on linkedin sir ")
    elif there_exists(["open feed"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/feed/"
        webbrowser.get().open(url)
        engine_speak("opening your linkedin feed sir ")
    elif there_exists(["open network"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/mynetworks/"
        webbrowser.get().open(url)
        engine_speak("opening your network on linkedin sir ")
    elif there_exists(["on linkedin"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/search/results/all/?keywords="+search_term
        webbrowser.get().open(url)
        engine_speak("here what i found for"+search_term+"on linkedin sir")
    elif there_exists(["show my connections"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/mynetworks/invite-connect/connections/"
        webbrowser.get().open(url)
        engine_speak("here you can see you connections on linkedin ")
    elif there_exists(["jobs"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/jobs/"
        webbrowser.get().open(url)
        engine_speak("opening job section on linkedin sir")
    elif there_exists(["linkedin messages"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/messaging/"
        webbrowser.get().open(url)
        engine_speak("opening your message section on linkedin sir ")
    elif there_exists(["linkedin notifications"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/notifications/"
        webbrowser.get().open(url)
        engine_speak("opening your network on linkedin sir ")
    elif there_exists(["linkedin settings"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/psettings/"
        webbrowser.get().open(url)
        engine_speak("opening your settings on linkedin sir")
    elif there_exists(["learning"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.linkedin.com/learning/"
        webbrowser.get().open(url)
        engine_speak("opening linkedin learning sir ")
    
        
    #8 time table
    if there_exists(["show my time table"]):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()
    
    #9 weather
    if there_exists(["weather","tell me the weather report","whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
    
    #open gmail
    if there_exists(["open my mail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")
    
    #News tv channels 
    if there_exists(["news7"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.tvhub.in/watch/news7-tamil-live.html"
        webbrowser.get().open(url)
        engine_speak("opening news7 tamil channel")
    elif there_exists(["polimer news"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.tvhub.in/watch/polimer-news-live.html"
        webbrowser.get().open(url)
        engine_speak("opening polimer news tamil channel")
    elif there_exists(["sun news"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.tvhub.in/watch/sun-news-live.html"
        webbrowser.get().open(url)
        engine_speak("opening sun news tamil channel")
    elif there_exists(["new generation"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.tvhub.in/watch/puthiya-thalaimurai-live.html"
        webbrowser.get().open(url)
        engine_speak("opening puthiya thalaimurai news tamil channel")
    elif there_exists(["news 18 tamilnadu"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.tvhub.in/watch/news18-tamilnadu-live.html"
        webbrowser.get().open(url)
        engine_speak("opening news 18 tamilnadu channel")
    elif there_exists(["daily post channel"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.onlinechannels.live/thanthi-tv/"
        webbrowser.get().open(url)
        engine_speak("opening daily thanthi tamil news channel")
    

    #10 stone paper scisorrs
    
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

    #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

    #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
        
    #13 screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/YASH/Pictures/Screenshots') 
    
    
    #14 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition=record_audio("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found '+definitions[1])
            else:
                engine_speak ('Here is what i found '+definitions[2])
        else:
                engine_speak("im sorry i could not find the definition for "+definition)
    
    if there_exists(["write up a mail"]):
        mail()

    if there_exists(["whatsapp message"]): 
        engine.say("Enter receivers number")
        engine.runAndWait()
        msg()
        print("Scan QR code with your phone")
        engine.say("Scan QR code with your phone")
        engine.say("message will be sent soon")
        engine.runAndWait()

    if there_exists(["top headlines"]):
        news()
    if there_exists(["jokes"]):
        joke = pyjokes.get_joke()
        engine_speak("here are some jokes for you")
        engine_speak(joke)

    if there_exists(["take down the notes"]):
        engine_speak("what i want to take as notes?")
        notes = record_audio()
        f = open('notepad.exe', 'w')
        f.write(notes)
        engine_speak("your notes are saved")
    
    if there_exists(["show me the notes"]):
        engine_speak("your saved note is opening now")
        f = open('notepad.exe','r')
        f.read()
        print(f.read())
        engine_speak(f.read())

    if there_exists(["take my plan"]):
        engine_speak("what i want remember you")
        memory = record_audio()
        engine_speak("your plan"+memory)
        remember = memory
        remember = open('memory.txt','w')
        remember.close()

    if there_exists(["do i have any plan"]):
        remember = open('memory.txt','r')
        engine_speak("you asked me to remember"+remember.read())

    if there_exists(["logout"]):
        os.system("shutdown -1")

    if there_exists(["restart"]):
        os.system("shutdown /r/t 1")

    if there_exists(["shutdown"]):
        os.system("shutdown /s/t 1")


    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("thanks for using me, hope we will meet soon in future... ")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Shayera'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("what can i do for you") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond

