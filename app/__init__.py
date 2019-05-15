from flask import Flask

# Initialise app
app = Flask(__name__)

# Load config
app.config.from_object('config.DevelopmentConfig')

# Load views
from app import views