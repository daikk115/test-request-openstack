from os.path import getmtime
import json

import env
from graceful_exit import *

## CONFIG
ACCOUNT = 'AUTH_4802b3a577b344be8b77fc27a359bf58'  # Run 'swift stat' command to see ACCOUNT
CONTAINER = 'daidv'
OBJECT = 'test_object'
path = 'test_object'
url = 'http://{}:8080/v1/{}/{}?format=json&prefix=delete_objects'.format(env.IP, ACCOUNT, CONTAINER)

put_headers = {
    'x-object-meta-mtime': "%f" % getmtime(path),
    'X-Auth-Token': env.TOKEN
}

headers = {
    'X-Auth-Token': env.TOKEN
}

## RUN
if __name__ == '__main__':
    future = send_request(url, 'GET', headers=headers)
    list_obs = []
    for ob in json.loads(future.result().content):
        list_obs.append(ob.get('name'))
    print list_obs

