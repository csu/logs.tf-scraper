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

def get_match_metadata(min, page=False):
	result = {}
	url = constants.HOMEPAGE + "?p=%d" % page if page else constants.HOMEPAGE
	soup = BeautifulSoup(requests.get(url).text)
	rows = soup.find_all('tr')
	for i in range(1, len(rows)):
		cols = rows[i].find_all('td')
		match_id = int(cols[0].a.get('href')[1:])

		# stop if this is the last log
		if min == match_id:
			return result, True

		match_name = cols[0].get_text()
		map_name = str(cols[1].get_text())
		game_type = str(cols[2].get_text())
		datetime = int(cols[4].get('data-timestamp'))
		result[match_id] = {
			'title': match_name,
			'map': map_name,
			'type': game_type,
			'datetime': datetime
		}
	return result, False