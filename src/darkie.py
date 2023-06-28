"""
Search keyword "drugs" in default search engine (default = "ahmia") and save the results in "op.csv":
python darkie.py -k drugs -f op.csv

Search keyword "drugs" in default search engine (default = "ahmia") and save the results in "op.txt":
python darkie.py -k drugs -f op.txt

Search keyword "redline stealer" in default search engine (default = "ahmia") and save the results in "op.csv":
python darkie.py -k "redline stealer" -f op.csv

Search keyword "drugs" in given search engine "ahmia" and save the results in "op.csv":
python darkie.py -k drugs -e ahmia -f op.csv

Search keyword "drugs" in given search engine "onionland" and save the results in "op.csv":
python darkie.py -k drugs -e onionland -f op.csv

Search keyword "drugs" in given search engine "excavator" and save the results in "op.txt":
python darkie.py -k drugs -e excavator -f op.txt

Search keyword "drugs" in given search engines "ahmia", "onionland", "excavator" and save the results in "op.csv":
python darkie.py -k drugs -e ahmia onionland excavator -f op.csv

Search keyword "drugs" in all available search engines (ahmia, onionland, excavator, onionengine, venus) and save the results in "op.csv":
python darkie.py -k drugs -a -f op.csv
"""

import argparse
import sys

# Custom imports
from modules import search
from modules import tor
from modules import statics
from modules import process
from modules import file
from modules.utils import showBanner
from modules.process import parse_url
from tqdm import tqdm

# Setup Argparser
parser = argparse.ArgumentParser(description='Darkie Search Control')

# Search <keyword>
parser.add_argument('-k', '--keyword', type=str, metavar='',
                    required=True, help='Search Keyword')

engineHelpText = "Search engine name (Available search engines : " + ", ".join(statics.SEARCH_ENGINES) + ")"
# Search specific search <engine>
parser.add_argument('-e', '--engine', type=str, nargs='+', metavar='',
                    required=False, help=engineHelpText)

# Search all search engines (flag)
parser.add_argument('-a', '--all', required=False, action="store_true",
                    help='Search using all available engine(s)')

# Download media from onion url (flag)
parser.add_argument('-d', '--download', required=False, action="store_true",
                    help='Download all media from onion url(s)')

# Save onion urls to <filename>
parser.add_argument('-f', '--filepath', type=str, metavar='',
                    required=True, help='Save onion urls in given filepath')

args = parser.parse_args()

class Darkie():
    def __init__(self):
        self.keyword = args.keyword  # required
        self.engine = args.engine # if not provieded then use default = 'ahmia'
        self.all = args.all
        self.download = args.download
        self.filepath = args.filepath  # required
        self.engineList = self.__getEngineList()

    def __getEngineList(self, ):
        engineList = []
        if self.all:
            # use all search engines
            engineList = statics.SEARCH_ENGINES
        elif self.engine:
            engineList = self.engine
        else:
            # use default search engines
            engineList = [statics.DEFAULT_SEARCH_ENGINE]
            # print(engineList)

        return engineList

    def __searchKeyword(self, engine, keyword):
        """
        Search keyword in given search engine and returns the onion links
        """
        data = None
        onionLinks = []
        
        searchEngine = engine.lower()
        if searchEngine == statics.AHMIA_SEARCH_ENGINE:
            data = search.ahmia(keyword)
        elif searchEngine == statics.ONIONLAND_SEARCH_ENGINE:
            data = search.onionland(keyword)
        elif searchEngine == statics.EXCAVATOR_SEARCH_ENGINE:
            data = search.excavator(keyword)
        elif searchEngine == statics.ONIONENGINE_SEARCH_ENGINE:
            data = search.onionengine(keyword)
        elif searchEngine == statics.VENUS_SEARCH_ENGINE:
            data = search.venus(keyword)
        else:
            print(
                f"{statics.R}Please give a valid search engine from {statics.SEARCH_ENGINES}{statics.W}")

        if data != None:
            # List of onion urls after scraping it from the given search engine data
            onionLinks = process.scrapOnionLinks(keyword, searchEngine, data)

        return onionLinks

    def __validateOnionLinks(self, onionLinks):
        validatedUrls = []
        for data in tqdm(onionLinks):
            # Parsing url
            parsed = parse_url(data["URL"], self.download)
            if parsed:
                validatedUrls.append(data)
            # if self.download:
            #     print("Download Media for {}".format(data["URL"]))
            # validatedUrls.append(data)

        return validatedUrls

    def __searchAllEngines(self, ):
        """
        Search keyword in all given engines and then save it to a file
        """
        allOnionLinks = []
        for engine in self.engineList:
            engine = engine.lower()
            print(statics.C)
            print(f"Searching in '{engine}'.")
            print(statics.W)
            onionLinks = self.__searchKeyword(engine, self.keyword)
            validatedUrls = self.__validateOnionLinks(onionLinks)
            allOnionLinks.extend(validatedUrls)
            print(f"Found {len(allOnionLinks)} onion links.")
            print(f"Searching for {engine} done!")
            print()
        
        # Save the onion links to filepath
        # try:
        ext = self.filepath.split(".")[-1]
        # print(ext)
        if ext == "txt":
            file.saveOnionLinksToTxtFile(allOnionLinks, self.filepath)
        elif ext == "csv":
            file.saveOnionLinksToCSVFile(allOnionLinks, self.filepath)
        else:
            print(statics.INVALID_FILE_PATH)
        # except:
        #     print(statics.INVALID_FILE_PATH)

    def start(self, ):
        if len(self.engineList) > 0:
            self.__searchAllEngines()
        else:
            print("Please enter a valid search engine!")
            print("Current available search engines : ", statics.SEARCH_ENGINES)
            print()

def run():
    showBanner()
    tor.checkServiceStatus()
    tor.connectTor()
    darkie = Darkie()
    darkie.start()


if __name__ == '__main__':
    run()
