import requests


r = requests.get("https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content_viza = ""
content = data.find_all("div", {"class": "article_body"})
for i in content:
    try:
        content_viza+=i.text
    except:
        pass


