import requests

from keyboards.inline.parser import parse

r = requests.get("https://www.mzv.cz/moscow/ru/informacija_o_CR/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content = data.find_all("h2", {"class": "article_title"})
pol_articles = {}
for i in content:
    pol_articles[i.getText()] = "https://www.mzv.cz" + i.a["href"]


