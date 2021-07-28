import requests

url = "https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/konsulskije_sbory/index.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
fee_list = ""
fee_content = data.find_all("div", {"class": "article_body"})
for i in fee_content:
    try:
        fee_list+=i.text
    except:
        pass

