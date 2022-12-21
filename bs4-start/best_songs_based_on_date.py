import requests
from bs4 import BeautifulSoup
import random as r
from webbrowser import open_new_tab

import spotipy
from spotipy.oauth2 import SpotifyOAuth

a=input("Enter the date you wanna search the songs for in yyyy-mm-dd format")
query="https://www.billboard.com/charts/hot-100/"+a+"/"
res=requests.get(query)
content=res.text
soup=BeautifulSoup(content,'html.parser')

titles=soup.select(selector="li>#title-of-a-story")
open("songs.txt","w").close()

for i in titles:
   with open("songs.txt","a") as f:

     f.write(i.text.replace("\n","").replace("\t","")+"|")



with open("songs.txt","r") as f:
    arr=f.read().split("|")
open("songs.txt","w").close()
with open("songs.txt","a") as f:
    for i in arr:
        f.write(i+"\n")

with open("songs.txt","r") as f:
    k=f.read().splitlines()
    str=k[r.randint(0,101)]
    query="https://www.youtube.com/results?search_query="+str
    print(query)
    open_new_tab(query)
