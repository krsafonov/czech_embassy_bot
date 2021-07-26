import requests

url = "https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/postojannoe_prozhivanie/index.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
headers = data.find_all("h2", {"class": "article_title"})
constant = {}
for i in headers:
    constant[i.getText()] = "https://www.mzv.cz" + i.a["href"]
