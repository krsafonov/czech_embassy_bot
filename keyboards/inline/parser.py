import requests
from telegraph_page_maker import create_page


def parse(page_url):
    r = requests.get(page_url)
    r.encoding = 'utf-8-sig'
    from bs4 import BeautifulSoup
    data = BeautifulSoup(r.content, features='html.parser')
    content = list(data.find("div", {"class": "article_body"}).children)
    title = data.find("h1", {"class": "article_title"})
    for tag in content:
        if tag.name == "h1" or tag.name == "h2":
            tag.name = "h4"

    if not tag.name in ['a', 'aside', 'b', 'blockquote', 'br', 'code', 'em', 'figcaption', 'figure',
        'h3', 'h4', 'hr', 'i', 'iframe', 'img', 'li', 'ol', 'p', 'pre', 's',
        'strong', 'u', 'ul', 'video']:
                list(content).remove(tag)
        
    content = map(str, content)
    html_content = "\n".join(content)
    return create_page(title, html_content)


