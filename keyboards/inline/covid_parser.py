import requests


r = requests.get("https://www.mzv.cz/moscow/ru/vizy_i_konsulskaja/covid_19/index.html")
r.encoding = 'utf-8-sig'
from bs4 import BeautifulSoup
data = BeautifulSoup(r.text, features='html.parser')
content = data.find_all("h2", {"class": "article_title"})
list5 = {}
for i in content:
    list5[i.getText()] = "https://www.mzv.cz" + i.a["href"]


"""def get_covid_article(num):
    url = list(list5.values())[num-1]
    r = requests.get(url)
    r.encoding = 'utf-8-sig'
    from bs4 import BeautifulSoup
    data = BeautifulSoup(r.text, features='html.parser')
    article_content = ""
    par = list(data.find("div", {"class": "article_body"}).children)
    for i in par:
        try:
            article_content += i.text
        except:
            pass

    return article_content"""