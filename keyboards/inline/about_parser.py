import requests

from telegraph_page_maker import create_page

r = requests.get("https://www.mzv.cz/moscow/ru/o_posolstve/kak_nas_najti.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')

content = str(data.find("div", {"class": "article_body"}))
title = data.find("h1", {"class": "article_title"})


about = create_page(title.text, "\n".join(content.split("\n")[1:-1]))