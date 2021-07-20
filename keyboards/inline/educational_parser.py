import requests


r = requests.get("https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/covid_19/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content1 = data.find_all("div", {"class": "article_content"}, {"p"})
print(content1)