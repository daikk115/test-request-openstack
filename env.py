from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

IP = '10.164.178.141'
USERNAME = 'admin'
PASSWORD = '1'
PROJECT_NAME = 'admin'
AUTH_URL = 'http://{}:5000/v3'.format(IP)

auth = v3.Password(auth_url=AUTH_URL,
                    user_domain_name='default',
                    username=USERNAME,
                    password=PASSWORD,
                    project_domain_name='default',
                    project_name=PROJECT_NAME)

session = session.Session(auth=auth)
TOKEN = session.get_token()
