import datetime
import wikipedia
import pywhatkit
import webbrowser
import keyboard

import speak
from speak import Spk
from listen import takeCommand
import pyautogui
import os
from NeuralNetwork import tokenize
import random
import requests
import bs4



# task function

def time():
    time = datetime.datetime.now().strftime("%H:%M")
    print(time)
    Spk.say(time)

def date():
    date = datetime.date.today()
    print(date)
    Spk.say(date)

def day():
    day = datetime.datetime.now().strftime("%A")
    Spk.say(day)

def ss():
    Spk.say("ok sir, what should I name that file?")
    fname = takeCommand()
    path = fname + ".jpg"
    fullpath = "C:\\Users\\Sdewa\\OneDrive\\Pictures\\Screenshots\\" + path
    kk = pyautogui.screenshot()
    kk.save(fullpath)
    os.startfile("C:\\Users\\Sdewa\\OneDrive\\Pictures\\Screenshots")
    Spk.say("here is your screen shot")

def openApp(query):
      Spk.say("ok sir, wait a second..")
      print(query)
      query = query.replace("open","")
      if "vs code" in query:
          os.startfile('C://Users//Sdewa//AppData//Local//Programs//Microsoft VS Code//code.exe')
          Spk.say("done sir")
      if "pycharm" in query:
          os.startfile("C://Program Files//JetBrains//PyCharm Community Edition 2022.1//bin//pycharm64.exe")
          Spk.say("done sir")
      if "netbeans" in query:
          os.startfile("C://Program Files//NetBeans-13//netbeans//bin//netbeans64.exe")
          Spk.say("done sir")
      if "this pc" in query:
          os.startfile("This PC")
          Spk.say("done sir...")
      if "chrome" in query:
          os.startfile("C://Program Files (x86)//Google//Chrome//Application//chrome.exe")
          Spk.say("done sir....")
      if "cmd" in query:
          os.startfile("C://Users//Sdewa//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//System Tools//Command Prompt.lnk")
          Spk.say("done sir...")
      if "control panel" in query:
          os.startfile("C://Users//Sdewa//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//System Tools//Control Panel.lnk")
          Spk.say("done sir....")
      if "notepad plus plus" in query:
          os.startfile('C://ProgramData//Microsoft//Windows//Start Menu//Programs//Notepad++.lnk')
          Spk.say("done sir....")
      if "task manager" in query:
          os.startfile('C://ProgramData//Microsoft//Windows//Start Menu//Programs//System Tools//Task Manager.lnk')

def Music():
     music_dir = 'C://Users//Sdewa//Music//my music//english song'
     songs = os.listdir(music_dir)
     print(songs)
     os.startfile(os.path.join(music_dir, songs[0]))  # we can use random module to play song randomly

def msgWhatsappp():
    Spk.say("tell me the name of the person")
    name = takeCommand()
    if "tarun2" in name:
        Spk.say("tell me the massage")
        msg = takeCommand()
        Spk.say("tell me the the time in hour!")
        hour = int(takeCommand())
        Spk.say("tell me the time in minute")
        minute = int(takeCommand())
        pywhatkit.sendwhatmsg("+919767260520",msg,hour,minute,20)
        Spk.say("ok sir! sending whatsapp massage")

    elif "sanju bhai" in name:
        Spk.say("tell me the massage")
        msg = takeCommand()
        Spk.say("tell me the the time in hour!")
        hour = int(takeCommand())
        Spk.say("tell me the time in minute")
        minute = int(takeCommand())
        pywhatkit.sendwhatmsg("+918717875390", msg, hour, minute, 20)
        Spk.say("ok sir! sending whatsapp massage")

    else:
        Spk.say("tell me the massage")
        msg = takeCommand()
        Spk.say("tell me the phone number")
        phone = int(takeCommand())
        Spk.say("tell me the the time in hour!")
        hour = int(takeCommand())
        Spk.say("tell me the time in minute")
        minute = int(takeCommand())
        pywhatkit.sendwhatmsg("91"+phone, msg, hour, minute, 20)
        Spk.say("ok sir! sending whatsapp massage")

def youtubeAuto():
    speak.Spk.say("whats your command..")
    cmd = takeCommand()

    if "pause" in cmd:
        keyboard.press("space bar")
    elif "restart" in cmd:
        keyboard.press('0')
    elif "mute" in cmd:
        keyboard.press('m')
    elif "forward" in cmd:
        keyboard.press('l')
    elif "back" in cmd:
        keyboard.press('j')
    elif "fullscreen" in cmd:
        keyboard.press('f')
    elif "minimize screen" in cmd:
        keyboard.press('t')
    speak("done sir...")

def chromeAuto():
    speak.Spk.say("whats your command")
    cmd = takeCommand()
    if "new tab" in cmd:
        keyboard.press_and_release('ctrl + t')
    elif "close curent tab" in cmd:
        keyboard.press_and_release('ctrl + w')
    elif "new window" in cmd:
        keyboard.press_and_release('ctrl + n')
    elif "history" in cmd:
        keyboard.press_and_release('ctrl + h')
    elif "download" in cmd:
        keyboard.press_and_release('ctrl + j')

def classroom():
    webbrowser.open('https://classroom.google.com/u/0/h')
    speak.Spk.say("done sir...")

def gmail():
    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    speak.Spk.say("done sir.")



#non input function
def NonInputFn(query):
    query = str(query)
    if "time" in query:
        time()
    elif "date" in query:
        date()
    elif "day" in query:
        day()
    elif "screenshot" in query:
        ss()

    elif "music" in query:
        Music()

    elif "whatsapp" in query:
        msgWhatsappp()

    elif "classroom" in query:
        classroom()

    elif "gmail" in query:
        gmail()

    elif "play on youtube" in query:
        Spk.say("which song you want to listen sir?")
        song_name = takeCommand()
        pywhatkit.playonyt(song_name)


# input function
def InputFn(reply,query):
    if "wikipedia" in reply:
        query = str(query).replace("who is", "").replace("how to","").replace("what is","").replace("about","").replace("according to","").replace("wikipedia","").replace("according to wikipedia","")
        try:
            Spk.say("sir, what you want to searcgh in wikipedia...")
            wps=''
            while len(wps)==0 and wps=="":
                Spk.say("sir please provide me, search element....")
                wps += takeCommand()


            #url = "https://www.google.com/search?q=" + wps
            #r = requests.get(url)
            #data = bs4.BeautifulSoup(r.text, 'html.parser')

            #result = data.findAll("div",class_="FLP8od").text
            result = wikipedia.summary(wps, sentences=2)
            Spk.say(result)
        except Exception as err:
                Spk.say(err)


    elif "google" in reply:
        query = query.replace("in google","").replace("on","").replace("google","").replace("search","").replace("google search","").replace("according to google","").replace("accroding to","")
        Spk.say("sir, what you want to search on google....")
        gs=''
        while len(gs)==0 and gs=='':
            Spk.say("please sir, tell me search element..")
            gs += takeCommand()
        pywhatkit.search(gs)
        Spk.say("done sir...")

    elif "youtube" in reply:
        query = str(query).replace("in youtube","").replace("on youtube","").replace("youtube search","").replace("search on youtube","")
        Spk.say("sir, what you want to search on youtube....")
        yts=''
        while len(yts)==0 and yts=="":
               Spk.say("please tell me search element sir...")
               yts += takeCommand()
        list = ['play song','play a song','play music','entertain me','make my mood']
        #list2 = tokenize(list)
        list2 = random.choice(list)
        list3 = "".join(list)
        if yts in list:
            Spk.say("which song you want to enjoy, sir......")
            song_name = ''
            while len(song_name)==0 and song_name=='':
                  Spk.say("please sir tell me song name...")
                  song_name=takeCommand()
            Spk.say("ok sir, I am playing songs")
            pywhatkit.playonyt(song_name)
        else:
          webbrowser.open("https://www.youtube.com/results?search_query=" + yts)
          speak.Spk.say("done sir...")
    elif "make food" in reply:
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)

    elif "open app" in reply:
        openApp(query)











