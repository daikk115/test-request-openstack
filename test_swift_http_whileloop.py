import json

import env
from graceful_exit import *

## CONFIG
ACCOUNT = 'AUTH_e606c8d68a2c499a9b9c90e1cdd836b8'  # Run 'swift stat' command to see ACCOUNT
CONTAINER = 'daidv'
path = 'test_object'

headers = {
    'X-Auth-Token': env.TOKEN
}

update_headers = {
    'X-Auth-Token': env.TOKEN,
    'X-Object-Meta-test': 'testing object'
}

## RUN
if __name__ == '__main__':
    # Meanwhile upload an object, we can't update metadata or delete,
    # so we will separate uploading with delete or update job.

    # One object for update test
    update_object = 'update_object'
    # Get object list for delete test: delete_object.*
    url = 'http://{}:8080/v1/{}/{}?format=json&prefix=delete_objects'.format(env.IP, ACCOUNT, CONTAINER)
    future = send_request(url, 'GET', headers=headers)
    list_delete_objects = []
    for ob in json.loads(future.result().content):
        list_delete_objects.append(ob.get('name'))

    i = 0
    while True:
        time.sleep(0.3)
        # Create object
        create_url = 'http://{}:8080/v1/{}/{}/{}'.format(env.IP, ACCOUNT, CONTAINER, i)
        send_request(create_url, 'PUT',
                     headers=headers, data="Dang Van Dai")
        i += 1

        # Delete object
        try:
            delete_object = list_delete_objects.pop(0)
        except:
            # In case, we don't have any object in delete list
            continue
        # Get and update an object
        delete_url = 'http://{}:8080/v1/{}/{}/{}'.format(env.IP, ACCOUNT, CONTAINER, delete_object)
        send_request(delete_url, 'GET', headers=headers)
        send_request(delete_url, 'POST', headers=headers)
        send_request(delete_url, 'DELETE', headers=headers)
