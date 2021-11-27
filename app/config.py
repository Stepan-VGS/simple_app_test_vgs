import os


class Config(object):
    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')
    VAULTID = os.environ.get('VAULTID')
    DEBUG = True

