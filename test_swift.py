import requests

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

username = 'admin'
password = '1'
project_name = 'admin'
auth_url = 'http://10.164.178.141:5000/v3'

auth = v3.Password(auth_url=auth_url,
		    user_domain_name='default',
                    username=username,
                    password=password,
		    project_domain_name='default',
                    project_name=project_name)

session = session.Session(auth=auth)
token = session.get_token()

url = 'http://10.164.178.141:8080/v1/AUTH_383cff4655cb489db05018236eb26826/DAIKK/blue-green.png'

headers = {
  'X-Auth-Token': token
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    print("Download OK")
else:
    print("Download fail")
