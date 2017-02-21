import ceilometerclient.client

VERSION = '2'
USERNAME = 'admin'
PASSWORD = '1'
PROJECT_NAME = 'admin'
AUTH_URL = 'http://10.164.178.141:5000/v3'

cclient = ceilometerclient.client.get_client(
	VERSION,
	os_username=USERNAME,
	os_password=PASSWORD,
	os_tenant_name=PROJECT_NAME,
	os_auth_url=AUTH_URL
)

print(cclient.meters.list())
