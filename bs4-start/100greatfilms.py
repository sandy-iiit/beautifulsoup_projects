import requests
from bs4 import BeautifulSoup

res=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content=res.text
soup=BeautifulSoup(content,"html.parser")

titles=soup.select(selector=".title",name="h3")
titles.reverse()
print(titles)
j=1
with open("100greatfilms.txt","a") as f:
    for i in titles:
        if j<101:
         f.write(i.text+"\n")
         j+=1
