import requests

import env
from graceful_exit import *


ACCOUNT = 'AUTH_17f007bcbbeb4c219cbeb4776302621c' #Run 'swift stat' command to see ACCOUNT
CONTAINER = 'DAIKK'
OBJECT = 'admin.sh'


url = 'http://{}:8080/v1/{}/{}/{}'.format(env.IP, ACCOUNT, CONTAINER, OBJECT)

headers = {
  'X-Auth-Token': env.TOKEN
}


if __name__ == '__main__':
    while(True):
    	time.sleep(0.3)
    	send_get_request(url, headers=headers)
