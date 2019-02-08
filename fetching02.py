# fetching01
import urllib.request

def fetching02():
    req = urllib.request.Request('http://www.voidspace.org.uk')
    response = urllib.request.urlopen(req)
    the_page = response.read()
    return the_page


# retrun make show inside this function.
