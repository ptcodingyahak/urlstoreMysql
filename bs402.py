# Fetching URLs
import random
import urllib.request
from bs4 import BeautifulSoup

def fetching01(contents):
    html = urllib.request.urlopen('https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99')
    response = BeautifulSoup(response, 'html.parser')
    return response

# return web page source changed html parser

links = fetching01("/wiki/컴퓨터과학")

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["herf"]
        print(newArticle)
        links = fetching01(newArticle)
except AttributeError:
    pass

finally:
    close()

# need to modify this code.
