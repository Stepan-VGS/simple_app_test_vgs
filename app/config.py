import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    your_tenant_id = os.getenv('your_tenant_id')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    
    
