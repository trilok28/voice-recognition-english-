import speech_recognition as sr  # to listen voice from microphone
import pyttsx3
from speak import Spk
import datetime
import ui


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        #Gui_start.self.gui.MainMsg_tb.setText("listening......")
        #print("listening....")
        Spk.say("listening....\n")
        r.pause_threshold=0.7
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,0,4)
    try:

        #print("Recognizing....")
        Spk.say("Recognizing....\n")
        query = r.recognize_google(audio, language='en-in')
        Spk.say("your command is : "+query+"\n")
        #print(f"your command {query}:\n")
        #speak.say("your command is " +query)
    except:
        return ""
    query = query.lower()
    query = str(query)
    return query
#takeCommand()

