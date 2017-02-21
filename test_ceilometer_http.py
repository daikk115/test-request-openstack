import requests

import env

url_list_meter = 'http://{}:8777/v2/meters'.format(env.IP)
url_get_statistics = 'http://{}:8777/v2/meters/storage.objects.outgoing.bytes/statistics'.format(env.IP)

headers = {
  'User-Agent': 'ceilometerclient.openstack.common.apiclient',
  'X-Auth-Token': env.TOKEN
}


r = requests.get(url_list_meter, headers=headers)
r2 = requests.get(url_get_statistics, headers=headers)

if r.status_code == 200:
    print("GET list meter OK")
else:
    print("GET list meter fail")

if r2.status_code == 200:
    print("GET statistics OK")
else:
    print("GET statistic fail")
