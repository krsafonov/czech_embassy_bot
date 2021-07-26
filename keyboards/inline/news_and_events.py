import requests


def events():
    url = "https://www.mzv.cz/moscow/ru/soobschenia_sobytija/index.html"
    r = requests.get(url)
    r.encoding = 'utf-8-sig'
    from bs4 import BeautifulSoup
    data = BeautifulSoup(r.text, features='html.parser')
    headers = data.find_all("h2", {"class": "article_title"})
    events_articels = {}
    for i in headers:
        events_articels[i.getText()] = "https://www.mzv.cz" + i.a["href"]
    return events_articels


