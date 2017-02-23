import requests
import time

from requests_futures.sessions import FuturesSession

import env

ACCOUNT = 'AUTH_0064b9fb05d047e88d7a1fc900a9f8a7' #Run 'swift stat' command to see ACCOUNT
CONTAINER = 'DAIKK'
OBJECT = 'abc.txt'


url = 'http://{}:8080/v1/{}/{}/{}'.format(env.IP, ACCOUNT, CONTAINER, OBJECT)

headers = {
  'X-Auth-Token': env.TOKEN
}

fail = 0
success = 0


def bg_cb(sess, resp):
    print("%d - %s" % (time.time() * 1000, resp.status_code))

session = FuturesSession()
tasks = []

while(True):
	time.sleep(0.3)
	future = session.get(url, headers=headers, background_callback=bg_cb)
        tasks.append(future)

