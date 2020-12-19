import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    VAULT_ID = os.environ.get('VAULT_ID')
    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')
    VGS_SAMPLE_ECHO_SERVER = os.environ.get('VGS_SAMPLE_ECHO_SERVER')
    PORT = os.environ.get('PORT')

