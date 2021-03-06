import requests


def culture_articels():
    url = "https://www.mzv.cz/moscow/ru/kultura_obrazovanije/index.html"
    r = requests.get(url)
    r.encoding = 'utf-8-sig'
    from bs4 import BeautifulSoup
    data = BeautifulSoup(r.text, features='html.parser')
    headers = data.find_all("h2", {"class": "article_title"})
    cul_articels = {}
    for i in headers:
        cul_articels[i.getText()] = "https://www.mzv.cz" + i.a["href"]
    return cul_articels


