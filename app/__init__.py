# flask app
from flask import Flask

#needed for configuration options
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess' 

from app import routes