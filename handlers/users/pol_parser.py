import requests


def pol():
    url = "https://www.mzv.cz/moscow/ru/informacija_o_CR/index.html"
    r = requests.get(url)
    r.encoding = 'utf-8-sig'
    from bs4 import BeautifulSoup
    data = BeautifulSoup(r.text, features='html.parser')
    headers = data.find_all("h2", {"class": "article_title"})
    pol_articels = {}
    for i in headers:
        pol_articels[i.getText()] = "https://www.mzv.cz" + i.a["href"]
    return pol_articels


