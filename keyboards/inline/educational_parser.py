import requests


r = requests.get("https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/dolgosrochnaja/x2011_04_22_2.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.content, features='html.parser')
content = data.find("div", {"class": "article_body"})
ed_content = ""
for i in content:
    try:
        ed_content+=i.text
    except:
        pass
print(ed_content)

