from flask import Flask
from app.config import Config
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = 'static'

from app import routes
