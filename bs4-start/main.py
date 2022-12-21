import requests
from bs4 import BeautifulSoup

#
# with open("website.html") as f:
#     contents = f.read()
# # print(contents)
#
# soup=BeautifulSoup(contents,'html.parser')
# # print(soup.title.name)
# # print(soup.title.string)
#
# alltags=soup.findAll(name="a")
# # print(alltags)
# for i in alltags:
# # print(i.getText())
#   print(i.get("href"))
#
# heading=soup.find(name="h1",id="name")
# print(heading)
#
# section_heading=soup.find(name="h3",class_="heading")
# print(section_heading)
#
# name=soup.select_one(selector="#name")   #this is for a id
#
# print(name)
#
# link=soup.select(selector="p a") #this is for the links present inside the p tags
# print(link)
#
# heading=soup.select(".heading") #this is for a class..
#
# print(heading)


res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, 'html.parser')
article_titles = soup.select(selector=".titleline>a")
titles = []
links = []
scores = []
scores2=[]
article_scores = soup.select(selector=".score")

for i in article_titles:
    titles.append(i.text)
    links.append(i.get("href"))
for i in article_scores:
    scores.append(i.text.split(" "))

for i in scores:
    scores2.append(int(i[0]))
m = max(scores2)
arr = zip(titles, links, scores2)
for i, j, k in arr:
    if (k == m):
        print(f"Title:{i} \nLink:{j} \nscore:{k}")
