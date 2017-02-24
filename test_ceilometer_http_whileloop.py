import requests
import time

import env
from graceful_exit import *

url_list_meter = 'http://{}:8777/v2/meters'.format(env.IP)
url_get_statistics = 'http://{}:8777/v2/meters/storage.objects.outgoing.bytes/statistics'.format(env.IP)

headers = {
  'User-Agent': 'ceilometerclient.openstack.common.apiclient',
  'X-Auth-Token': env.TOKEN
}


if __name__ == '__main__':
    while(True):
    	time.sleep(0.3)
    	send_get_request(url_list_meter, headers=headers)
		send_get_request(url_get_statistics, headers=headers)
