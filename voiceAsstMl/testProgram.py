import wikipedia

#import listen
#import speak
#import random
import requests
from bs4 import BeautifulSoup
import bs4

#cmd = listen.takeCommand()
#list = ['play song','make my mood','play music']
#list2 = random.choice(list)
#list3= "".join(list2)
#print(list3)


#finding temprature and use in main.py file

# enter city name
city = "temprature in bilaspur chhattisgarh"
# create url
url = "https://www.google.com/search?q=" + city
# requests instance
r = requests.get(url)
# getting raw data
data = bs4.BeautifulSoup(r.text, 'html.parser')
temprature = data.find("div", class_ = "BNeawe").text
temprature2 = "current temp:"+temprature


try:
    wp ="what is java"
    result=wikipedia.summary(wp)
    print(result)
except Exception as ex:
    print(ex)

