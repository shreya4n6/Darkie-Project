from bs4 import BeautifulSoup
import re
import os
import requests
from modules import statics
from modules.utils import isOnionUrl, getUniqueString
from modules.search import session

def processScrappedLink(keyword, engine, scrappedLink, onionLinks):
    scrappedLinkList = scrappedLink.split("http")
    scrappedLink = "http" + ''.join(scrappedLinkList[1:])
    scrappedLink = scrappedLink.replace("\n", " ")
    scrappedLinkList = scrappedLink.split(" ")
    # print(scrappedLinkList)

    onionUrl = ""
    for sl in scrappedLinkList:
        if statics.ONION in sl:
            onionUrl = sl
            break

    # display the onion urls only
    if isOnionUrl(onionUrl):
        onionLinks.append({'Keyword':str(keyword), 'Engine':str(engine), 'URL':str(onionUrl)})


def scrapOnionLinks(keyword, engine, htmlDocument):
    # print(htmlDocument)

    onionLinks = []

    # create soap object
    soup = BeautifulSoup(htmlDocument, 'html.parser')

    for link in soup.find_all('a', attrs={'href': re.compile(".*http")}):
        scrappedLink = link.get('href')
        # print(scrappedLink)
        processScrappedLink(keyword, engine, scrappedLink, onionLinks)

    if engine == statics.ONIONLAND_SEARCH_ENGINE:
        for link in soup.find_all("div", class_="link"):
            scrappedLink = link.get_text()
            # print(scrappedLink)
            processScrappedLink(keyword, engine, scrappedLink, onionLinks)

    if engine == statics.EXCAVATOR_SEARCH_ENGINE:
        for link in soup.find_all("div", class_="mx-auto"):
            scrappedLink = link.get_text()
            # print(scrappedLink)
            processScrappedLink(keyword, engine, scrappedLink, onionLinks)

    if engine == statics.VENUS_SEARCH_ENGINE:
        for link in soup.find_all("div", class_="Onionsite-footer"):
            scrappedLink = link.get_text()
            # print(scrappedLink)
            processScrappedLink(keyword, engine, scrappedLink, onionLinks)

    return onionLinks


def parse_url(torurl, down):
    """
    Scrapes website url defined by user
    """
    url_media = []
    try:
        try:
            # torurl = input(C + '[+] '+ G + 'Please Enter URL -> ' +W)
            if 'http://' in torurl:
                response = session.get(torurl).text
                soup = BeautifulSoup(response, 'lxml')
                tags = soup.find_all('img')
                for tag in tags:
                    urls = tag.get('src')
                    if 'http://' in urls:
                        media = str(urls)
                    else:
                        # media = torurl+'/'+str(urls)
                        media = torurl+str(urls)

                    url_media.append(media)
                    print(statics.C + "[>] " + statics.W + str(media))

                # down = input(C + '[+] '+ G + 'Download Media (y/n) -> ')
                torurl1 = torurl.split('.onion')[0]
                torurl1 = torurl1.replace('http://','')
                torurl1 = torurl1.replace('.','-')
                torurl1 = torurl1.replace('/','-')
                if down:
                    path = "Media/" + torurl1
                    os.makedirs(path, exist_ok=True)
                    # os.system('mkdir Media/{}'.format(torurl1))
                    for item in url_media:
                        m = item.split('/')[-1]
                        # m = getUniqueString()
                        if '.png' or '.jpg' or '.gif' in m:
                            r = session.get(item)
                            with open('Media/{}/{}'.format(torurl1,m), 'wb') as f:
                                f.write(r.content)
                    print('\n' + statics.C + '[>] All Media Downloaded -> ' + statics.G + 'Media/'+torurl1 + statics.W)
                else:
                    # print('\n' + statics.R + '[!] Exiting...')
                    # exit()
                    pass
                
                # If url data is fetched properly
                return True
        except requests.exceptions.ContentDecodingError as e:
            print(statics.R +'[!] Content Decoding Error in {}'.format(torurl) + statics.W)
            pass
        except requests.exceptions.ConnectionError as e:
            print(statics.R +'[!] Connection Error in {}'.format(torurl) + statics.W)
            pass
    except requests.exceptions.InvalidURL as e:
        print(statics.R +'[!] Invalid URL{}'.format(torurl) + statics.W)
        pass

    # If there's an error
    return False