import sys
import time
import requests
import pyttsx3
from bs4 import BeautifulSoup

engine = pyttsx3.init()
engine.setProperty('rate',160)

time = int(time.strftime("%H"))
if 4<=time<12:
    print("\n                 Good Morning, I'm your news reader assistant")
    engine.say("Good Morning, I'm your news reader assistant")
    engine.runAndWait()
elif 12<=time<=15:
    print("\n                 Good Afternoon, I'm your news reader assistant")
    engine.say("Good Afternoon, I'm your news reader assistant")
    engine.runAndWait()
elif 15<time<19:
    print("\n                 Good Evening, I'm your news reader assistant")
    engine.say("Good Evening, I'm your news reader assistant")
    engine.runAndWait()
elif 19<=time<4:
    print("\n         Hi, Its quite late but I'll tell you all important headlines ASAP")
    engine.say("Hi, Its quite late but I'll tell you all important headlines ASAP")
    engine.runAndWait()

print("\n1.NDTV\n2.India Today\n3.Hindustan Times\n")

print("Select any source for your daily news :  ")
engine.say("Select any source for your daily news")
engine.runAndWait()
choice = int(input())




if choice == 1:
    url = "https://www.ndtv.com/top-stories"  #get website from user
    attributes = {'class': 'nstory_intro'}
elif choice == 2:
    url = "https://www.indiatoday.in/top-stories"
    attributes = {'class': 'detail'}
elif choice == 3:
    url = "https://www.hindustantimes.com/top-news/"
    attributes = {'class': 'wclink2'}

content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')
data = soup.findAll('div', attributes)   # data = soup.findAll('div', {'class': 'nstory_intro'})

a = ""
count = 0
j = 0
for i in range(len(data)):
    count = count + 1
    print("\n",count,"-",data[j].text,"\n")
    a = a + data[j].text
    j = j + 1
if 7<=time<4: 
    print("             \nGood Night!")

engine.say(a)
engine.runAndWait()