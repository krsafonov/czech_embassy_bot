def trade_articles():
    pass
import requests



url = "https://www.mzv.cz/moscow/ru/torgovlja_ekonomika/index.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
headers = data.find_all("h2", {"class": "article_title"})
trade_articels = {}
for i in headers:
    trade_articels[i.getText()] = "https://www.mzv.cz" + i.a["href"]
