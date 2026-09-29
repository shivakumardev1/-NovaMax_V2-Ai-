import webbrowser
from urllib.parse import quote_plus

def open_url(url):
    webbrowser.open(url)

def search(query):
    webbrowser.open("https://www.google.com/search?q=" + quote_plus(query))
