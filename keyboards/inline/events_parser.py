import requests


r = requests.get("https://www.mzv.cz/moscow/ru/soobschenia_sobytija/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content = data.find_all("div", {"class": "article_list"})
events = {}
for i in content:
    events[i.getText()] = "https://www.mzv.cz" + i.a["href"]



print(events)