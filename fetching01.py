# Fetching URLs
import urllib.request
response = urllib.request.urlopen('http://python.org')
html = response.read()
