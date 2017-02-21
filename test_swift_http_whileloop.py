import requests
import time

import env

ACCOUNT = 'AUTH_17f007bcbbeb4c219cbeb4776302621c' #Run 'swift stat' command to see ACCOUNT
CONTAINER = 'DAIKK'
OBJECT = 'admin.sh'


url = 'http://{}:8080/v1/{}/{}/{}'.format(env.IP, ACCOUNT, CONTAINER, OBJECT)

headers = {
  'X-Auth-Token': env.TOKEN
}

while(True):
	time.sleep(0.3)
	r = requests.get(url, headers=headers)
	if r.status_code == 200:
	    print("Download OK")
	else:
	    print("Download fail")

