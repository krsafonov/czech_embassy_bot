import requests

url = "https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/dolgosrochnaja/x2011_04_22_5.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
bis = ""
content = data.find_all("div", {"class": "article_body"})
for i in content:
    try:
        bis+=i.text
    except:
        pass
print(bis)