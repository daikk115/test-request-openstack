import requests

import env

url = 'http://192.168.122.150:8042/v2/alarms'

headers = {
  'X-Auth-Token': env.TOKEN
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    print("OK")
else:
    print("fail")
