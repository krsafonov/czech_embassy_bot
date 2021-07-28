import requests

url = "https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/index.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
basic_content = ""
content = data.find_all("div", {"class": "article_body"})
for i in content:
    try:
        basic_content+=i.text
    except:
        pass

print(basic_content)