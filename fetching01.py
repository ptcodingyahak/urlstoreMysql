#-*- coding: utf-8 -*-
# Fetching URLs
import urllib.request

def fetching01():
    utf= ('컴퓨터과학')
    kurl = utf.encode('UTF-8').decode('UTF-8')
    response = urllib.request.urlopen('https://ko.wikipedia.org/wiki/')
    html = response.read()
    return html
