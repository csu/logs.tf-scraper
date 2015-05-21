import requests
import constants

def get(match_id):
    return requests.get('%s%s' % (constants.API_DATA_BASE_URL, match_id)).text