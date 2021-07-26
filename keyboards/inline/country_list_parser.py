import requests

url = "https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/vizy_ne_nuzhny/index.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content = data.find_all("div", {"class": "article_body"})
clist = []
for i in content:
    clist.append(i)

