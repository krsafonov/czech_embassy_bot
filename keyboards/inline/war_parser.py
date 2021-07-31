import requests


r = requests.get("https://www.mzv.cz/moscow/ru/soobschenia_sobytija/x2020_04_03/index.html")
r.encoding = 'utf-8'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
war_content = ''
content = data.find_all("p", {"class": "article_perex"})
content1 = data.find_all("div", {"class": "article_body"})
for i in content:
    try:
        war_content+=i.text
    except:
        pass
for i in content1:
    try:
        war_content+=i.text
    except:
        pass
