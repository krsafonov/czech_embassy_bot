import requests

from telegraph_page_maker import create_page

url = "https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/vizovaja/dolgosrochnaja/x2011_08_17.html"
r = requests.get(url)
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content = str(data.find("div", {"class": "article_body"}))
title = data.find("h1", {"class": "article_title"})


differ = create_page(title.text, "\n".join(content.split("\n")[1:-1]))
