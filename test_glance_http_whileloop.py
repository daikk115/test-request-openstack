import json

import env
from graceful_exit import *

##################
##### CONFIG #####
##################
CHUNKSIZE = 1024 * 64  # 64kB
image_path = 'cirros-0.3.5-x86_64-disk.img'

# Create image data: use POST and PUT method.
# NOTE: put_data  and put_url will be formatted later
post_url = 'http://{}:9292/v2/images' .format(env.IP)
post_data = {
    "container_format": "bare",
    "disk_format": "qcow2",
    # more than one image can have similar name
    "name": "testing",
    "visibility": "public"
}
post_headers = {
    'X-Auth-Token': env.TOKEN,
    'Content-Type': 'application/json'
}

put_headers = {
    'X-Auth-Token': env.TOKEN,
    'Content-Type': 'application/octet-stream'
}

# Udate image: use PATCH method.
# NOTE: patch_url will be formatted later
patch_data = [{
    "path": "/name",
    "value": "testing_newname",
    "op": "replace"
}]
patch_headers = {
    'X-Auth-Token': env.TOKEN,
    'Content-Type': 'application/openstack-images-v2.1-json-patch'
}

# Delete image
# NOTE: get_url similar with patch_url
get_headers = {
    'X-Auth-Token': env.TOKEN
}

# Delete image
# NOTE: delete_url similar with patch_url
delete_headers = put_headers

################
def _chunk_body(body):
    # Source: https://github.com/openstack/python-glanceclient/blob/master/glanceclient/common/http.py#L62
    chunk = body
    while chunk:
        chunk = body.read(CHUNKSIZE)
        if not chunk:
            break
        yield chunk

if __name__ == '__main__':
    while True:
        time.sleep(0.1)
        # Create image
        try:
            future = send_request(post_url, 'POST',
                              headers=post_headers, data=json.JSONEncoder().encode(post_data))
            content = future.result().content
        except:
            # In case, we can't create image in database
            # or not graceful shutdown --> Connection Error
            continue
        image_id = json.loads(content).get('id')

        # Upload image binary data
        put_url = 'http://{}:9292/v2/images/{}/file'.format(env.IP, image_id)
        f = open(image_path, 'rb')
        chunk_data = _chunk_body(f)
        put_result = send_request(put_url, 'PUT',
                                  headers=put_headers, data=f, stream=True)
        # f.close()
        a = put_result.result().content

        # Update image
        patch_url = "http://{}:9292/v2/images/{}" .format(env.IP, image_id)
        send_request(patch_url, 'PATCH',
                     headers=patch_headers, data=json.JSONEncoder().encode(patch_data))

        # Get image
        get_url = patch_url
        send_request(get_url, 'GET',
                     headers=get_headers)

        # Delete image
        delete_url = patch_url
        send_request(delete_url, 'DELETE',
                     headers=delete_headers)




