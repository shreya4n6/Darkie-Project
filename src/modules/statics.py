VERSION = '1.0'

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'

ARG_ACTIONS = ["-k", "-e", "-a", "-f"]

AHMIA_SEARCH_URL = 'https://ahmia.fi/search/'
ONIONLAND_SEARCH_URL = 'https://onionlandsearchengine.com/search'
EXCAVATOR_SEARCH_URL = 'https://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion.ly/search'
ONIONENGINE_SEARCH_URL = 'https://onionengine.com/search.php?search='
VENUS_SEARCH_URL = 'https://venusoseaqnafjvzfmrcpcq6g47rhd7sa6nmzvaa4bj5rp6nm5jl7gad.onion.ly/Search?query='

AHMIA_SEARCH_ENGINE = 'ahmia'
ONIONLAND_SEARCH_ENGINE = 'onionland'
EXCAVATOR_SEARCH_ENGINE = 'excavator'
ONIONENGINE_SEARCH_ENGINE = 'onionengine'
VENUS_SEARCH_ENGINE = 'venus'

DEFAULT_SEARCH_ENGINE = AHMIA_SEARCH_ENGINE
SEARCH_ENGINES = [
    AHMIA_SEARCH_ENGINE,
    ONIONLAND_SEARCH_ENGINE,
    EXCAVATOR_SEARCH_ENGINE,
    ONIONENGINE_SEARCH_ENGINE,
    VENUS_SEARCH_ENGINE
]

ONION = ".onion"

INVALID_FILE_PATH = "Please provide a valid filepath with extension\nExample: `op.csv` or `op.txt`"