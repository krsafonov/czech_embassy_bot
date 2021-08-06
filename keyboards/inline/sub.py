import requests

r = requests.get("https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/novosti/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
headers = data.find_all("h2", {"class": "article_title"})
sub = {}
for i in headers:
    sub[i.getText()] = "https://www.mzv.cz" + i.a["href"]



def parse_article(new):
    url = list(headers.values())[new]
    r = requests.get(url)
    r.encoding = 'utf-8-sig'
    from bs4 import BeautifulSoup
    data = BeautifulSoup(r.text, features='html.parser')
    article_content = ""
    par = list(data.find("div", {"class": "article_body"}))
    for i in par:
        try:
            article_content += i.text
        except:
            pass

    return article_content