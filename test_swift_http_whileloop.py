from os.path import getmtime
import env
from graceful_exit import *

## CONFIG
ACCOUNT = 'AUTH_bc009afedb7b4ff0886b9bf18be3e733'  # Run 'swift stat' command to see ACCOUNT
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
    while True:
        time.sleep(0.1)
        # Create object
        f = open(path, 'rb')
        send_request(url, 'PUT',
                     headers=put_headers, data=f)
        f.close()
        # Update object
        #send_request(url, 'POST', headers=headers)
        # Get object
        send_request(url, 'GET', headers=headers)
        # Delete object
        send_request(url, 'DELETE', headers=headers)
