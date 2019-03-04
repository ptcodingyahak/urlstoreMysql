# Fetching URLs
import random
import urllib.request
from bs4 import BeautifulSoup

def fetching01(contents):
    html = urllib.request.urlopen("https://ko.wikipedia.org"+"contents")
    response = BeautifulSoup(html, 'html.parser')
    return response

# return web page source changed html parser

links = fetching01("/wiki/컴퓨터_과학")

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["herf"]
        print(newArticle)
        links = fetching01(newArticle)
except AttributeError:
    pass

# need to modify this code.
