# Fetching URLs

def fetching01():
    import urllib.request
    response = urllib.request.urlopen('http://python.org')
    html = response.read()
    return html
