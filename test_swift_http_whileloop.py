import requests
import time
import signal
import sys

from requests_futures.sessions import FuturesSession

import env

ACCOUNT = 'AUTH_17f007bcbbeb4c219cbeb4776302621c' #Run 'swift stat' command to see ACCOUNT
CONTAINER = 'DAIKK'
OBJECT = 'admin.sh'


url = 'http://{}:8080/v1/{}/{}/{}'.format(env.IP, ACCOUNT, CONTAINER, OBJECT)

headers = {
  'X-Auth-Token': env.TOKEN
}

fail = 0
success = 0
session = FuturesSession()
tasks = []

def bg_cb(sess, resp):
    print("%d - %s" % (time.time() * 1000, resp.status_code))


def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
	    for task in tasks:
		print(task.done())
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    signal.signal(signal.SIGINT, exit_gracefully)


if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)

    while(True):
    	time.sleep(0.3)
    	future = session.get(url, headers=headers, background_callback=bg_cb)
	tasks.append(future)
