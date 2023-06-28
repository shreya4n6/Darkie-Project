import requests
import cloudscraper
from modules import statics

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

def ahmia(query):
    # query = input("What you wanna search ? ")
    payload = {"q": query}
    r = requests.get(statics.AHMIA_SEARCH_URL, params=payload)
    # print(r.text)
    # print(r.status_code)
    # print(r.content)
    # print(r.json)
    # print()

    return r.text


def onionland(query):
    scraper = cloudscraper.create_scraper()
    # query = input("What u wanna search ? ")
    url = 'http://onionlandsearchengine.com/search?q='
    r = scraper.get(url + query)
    # print(r.text)
    # print()

    return r.text


def excavator(query):
    scraper = cloudscraper.create_scraper()
    # query = input("What u wanna search ? ")
    url = 'https://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion.ly/search/'
    r = scraper.get(url + query)
    # print(r.text)
    # print()

    return r.text


def onionengine(query):
    scraper = cloudscraper.create_scraper()
    # query = input("What u wanna search ? ")
    url = 'https://onionengine.com/search.php?search='
    r = scraper.get(url + query)
    # print(r.text)
    # print()

    return r.text


def venus(query):
    scraper = cloudscraper.create_scraper()
    # query = input("What u wanna search ? ")
    url = 'https://venusoseaqnafjvzfmrcpcq6g47rhd7sa6nmzvaa4bj5rp6nm5jl7gad.onion.ly/Search?query='
    r = scraper.get(url + query)
    # print(r.text)
    # print()

    return r.text