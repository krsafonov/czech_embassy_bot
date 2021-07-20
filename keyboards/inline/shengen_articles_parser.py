import requests


r = requests.get("https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/schengenskaja/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
page_content = data.find_all("h2", {"class": "article_title"})
shengen_articels = {}
for i in page_content:
    shengen_articels[i.getText()] = "https://www.mzv.cz" + i.a["href"]




