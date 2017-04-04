import requests

import env

#url = 'http://{}:8080/v1/{}/{}/{}'.format(env.IP, ACCOUNT, CONTAINER, OBJECT)
url = 'http://192.168.122.150:8041/v1/resource/generic?'

headers = {
  'X-Auth-Token': env.TOKEN
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    print("Download OK")
else:
    print("Download fail")
