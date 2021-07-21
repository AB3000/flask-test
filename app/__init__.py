# flask app
from flask import Flask
from config import Config

#needed for configuration options
app = Flask(__name__)
app.config.from_object(Config)

from app import routes