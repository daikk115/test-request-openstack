from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

IP = '192.168.122.150'
USERNAME = 'admin'
PASSWORD = '8XXumMXUe7JglJb4YQ7uHdokhJmvTw3YUJSGbFVY'
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
