import requests
import constants
from bs4 import BeautifulSoup

def get_dates(page_num):
    r = requests.get('%s?p=%s' % (constants.HOMEPAGE, page_num))
    r.raise_for_status()
    return r.text