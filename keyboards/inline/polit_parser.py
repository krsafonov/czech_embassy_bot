import requests


r = requests.get("https://www.mzv.cz/moscow/ru/informacija_o_CR/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content = data.find_all("h2", {"class": "article_title"})
polit = {}
for i in content:
    polit  [i.getText()] = "https://www.mzv.cz" + i.a["href"]

print(polit)
