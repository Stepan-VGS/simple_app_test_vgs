import os
from dotenv import load_dotenv
load_dotenv(override=True)

#enter your vault_id, username and password in the empty strings
class Config(object):
    your_tenant_id = os.environ.get('')
    USERNAME = os.environ.get('')
    PASSWORD = os.environ.get('')
    