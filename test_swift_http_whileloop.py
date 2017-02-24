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
    "Callback function when requests done"

    timestamp = time.time() * 1000
    tasks.append({
        "timestamp": timestamp,
        "status": resp.status_code
    })
    print("%d - %d" % (timestamp, resp.status_code))

def footer():
    "Return result of testing process"

    is_find_start = True
    count = 0
    start, end = 0, 0 # assign this vars prepare if we dont' have downtime

    for task in tasks:
        if is_find_start:
            if task.get('status') >= 400:
                is_find_start = False
                start = task.get('timestamp')
        else:
            count += 1
            if task.get('status') == 200:
                end = task.get('timestamp')
                break

    print("Downtime for rolling upgrade process: {} ms" .format(end-start))
    print("Number of fail requests (status: 503): {}" .format(count))


def exit_gracefully(signum, frame):
    # Source: Antti Haapala - http://stackoverflow.com/a/18115530
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            footer()
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
