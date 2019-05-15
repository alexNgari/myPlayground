# __init__.py

from flask import Flask
from flask_json import FlaskJSON

# Initialise app
app = Flask(__name__)

# Initialise FlaskJSON extension
json = FlaskJSON(app)

# Load config
app.config.from_object('config.DevelopmentConfig')

# Load views
from app import views