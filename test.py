from os.path import getmtime
import env
from graceful_exit import *

## CONFIG
ACCOUNT = 'AUTH_b10330b8ceb3428582840602142d2bd7'  # Run 'swift stat' command to see ACCOUNT
CONTAINER = 'daikk'
OBJECT = 'test_object'
path = 'test_object'
url = 'http://{}:8080/v1/{}/{}/{}'.format(env.IP, ACCOUNT, CONTAINER, OBJECT)

put_headers = {
    'x-object-meta-mtime': "%f" % getmtime(path),
    'X-Auth-Token': env.TOKEN
}

headers = {
    'X-Auth-Token': env.TOKEN
}

## RUN
if __name__ == '__main__':
    f = open(path, 'rb')
    future = send_request(url, 'PUT', headers=put_headers, data=f)
    f.close()
    # Update object
    #send_request(url, 'POST', headers=headers)
    # Get object
    #send_request(url, 'GET', headers=headers)
    # Delete object
    #send_request(url, 'DELETE', headers=headers)

