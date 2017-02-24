"""This script reponsible put all of send_get_request() function results
into list, gracefull exit any script import it and return analytics
"""
import time
import signal
import sys

from requests_futures.sessions import FuturesSession


tasks = []
session = FuturesSession()


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


def send_get_request(url, headers=None):
    session.get(url, headers=headers, background_callback=bg_cb)


original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exit_gracefully)
