import requests


r = requests.get("https://www.mzv.cz/moscow/ru/kultura_obrazovanije/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content = data.find_all("h2", {"class": "article_title"})
cul = {}
for i in content:
    cul[i.getText()] = "https://www.mzv.cz" + i.a["href"]

print(cul)
