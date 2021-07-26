import requests


r = requests.get("https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/dolgosrochnaja/x2011_04_22_2.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.content, features='html.parser')
content1 = data.findAll("div", class_ = "article_body")
dick = []
for i in content1:
    dick.append({
        "titel": data.find("p", class_ = "article_body").get_text(strip=True)
    })
print(titel)
