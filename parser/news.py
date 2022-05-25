# import requests
# from bs4 import BeautifulSoup
#
#
# URL = 'https://www.securitylab.ru/news/'
#
# HEADERS = {
#     "Accept": "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
#     }
#
# def get_html(url, params=''):
#     req = requests.get(url, headers=HEADERS, params=params)
#     return req
#
#
# print(get_html(URL))
#
# def get_data(html):
#     soup = BeautifulSoup(html, "html.parser")
#     items = soup.find_all('a', class_='article-card inline-card')
#     news = []
#     for item in items:
#         news.append({
#             'title': item.find("h2", class_='article-card-title').getText(),
#             'desc': item.find("p").getText(),
#             'link': "https://www.securitylab.ru/" + item.get('href'),
#             'time': item.find("time").getText()
#             # 'photo':  + item.find('div' ,class_ = "article-img").find('img')
#         })
#     return news
# def parser():
#     html = get_html(URL)
#     if html.status_code == 200:
#         news = []
#         for page in range(1,3):
#             html = get_html(f"{URL}page1_{page}.php")
#             news.extend(get_data(html.text))
#         # for i in get_data(html.text):
#         return news
#         #     print(i)
#     else:
#         raise Exception('ERROR in parser')
#
# parser()


import requests
from bs4 import BeautifulSoup

URL = 'https://rezka.ag/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

print(get_html(URL))


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='b-content__inline_item-link')
    news = []
    for item in items:
        news.append({
            'title': item.find("a").getText('href'),
            'desc': item.find("div").getText(),
            'link': "https://rezka.ag/" + item.get('href'),
            # 'time': item.find("time").getText()
        })
    return news



'https://rezka.ag/'


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for page in range(2):
            html = get_html(f"{URL}/page/{page}/")
            news.extend(get_data(html.text))
        # for i in get_data(html.text):
        return news
        #     print(i)
    else:
        raise Exception('ERROR in parser')

parser()





