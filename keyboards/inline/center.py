import requests

url = "https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/x2011_06_13/index.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
center_c = ""
center = data.find_all("div", {"class": "article_body"})
for i in center:
    try:
        center_c+=i.text
    except:
        pass

