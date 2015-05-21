import requests
import constants
from bs4 import BeautifulSoup

def get(match_id):
    r = requests.get('%s%s' % (constants.API_DATA_BASE_URL, match_id))
    r.raise_for_status()
    return r.text

def latest_match():
    soup = BeautifulSoup(requests.get(constants.HOMEPAGE).text)
    return int(soup.td.a.get('href')[1:])