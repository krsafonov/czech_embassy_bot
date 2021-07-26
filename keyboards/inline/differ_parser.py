import requests

url = "https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/dolgosrochnaja/x2011_08_17.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
differ = []
content = data.find_all("div", {"class": "article_body"})
for i in content:
    differ.append(i)
