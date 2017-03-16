import requests

import env
from graceful_exit import *

image_id = "9c615e3e-bd61-44fb-a1a1-351a3f19bee1"

url ="http://{}:9292/v2/images/{}" .format(env.IP, image_id)

headers = {
  'X-Auth-Token': env.TOKEN
}


if __name__ == '__main__':
    while(True):
    	time.sleep(0.3)
    	send_get_request(url, headers=headers)
