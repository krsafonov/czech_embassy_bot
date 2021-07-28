import requests


r = requests.get("https://www.mzv.cz/moscow/ru/o_posolstve/kak_nas_najti.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
about_content = ""
content = data.find_all("div", {"class": "article_body"})
for i in content:
    try:
        about_content+=i.text
    except:
        pass
