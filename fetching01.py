# Fetching URLs
import urllib.request

def fetching01():
    response = urllib.request.urlopen('https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99')
    html = response.read()
    return html
