import requests

def save_gt():
    r = requests.get("https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/index.html")
    r.encoding = 'utf-8-sig'
    from bs4 import BeautifulSoup
    data = BeautifulSoup(r.text, features='html.parser')
    content_viza = []
    content12 = data.find_all("div", {"class": "article_content"}, {"p"})
    for i in content12:
        content_viza.append(i)
