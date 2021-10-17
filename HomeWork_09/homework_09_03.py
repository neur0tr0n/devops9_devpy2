import datetime
from pprint import pprint

import requests
from datetime import datetime as dt
from datetime import timedelta as td


tag = 'python'
days_ago = 2
to_date = int(datetime.datetime(dt.now().year, dt.now().month, dt.now().day).timestamp())
from_date = int(to_date - td(days=days_ago).total_seconds())

HEADERS = {'Content-Type': 'application/json'}
PARAMS = {
    'fromdate': from_date,
    'todate': to_date,
    'order': 'desc',
    'sort': 'activity',
    'tagged': tag,
    'site': 'stackoverflow'
}
resp = requests.get('https://api.stackexchange.com/2.3/questions', headers=HEADERS, params=PARAMS)

for item in resp.json()['items']:
    print(item['title'], item['link'])


