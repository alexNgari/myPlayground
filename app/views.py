from flask import Flask, render_template, url_for
from app import app
from flask_json import FlaskJSON, json_response, JsonError, JsonRequest, as_json_p


# Route for home
@app.route('/')
def home():
    return render_template('index.html')


# Route for state-capital json data request
@app.route('/state-cap-data', methods = ['GET'])
@as_json_p
def getStateData():
    with app.open_resource('data/states.json') as f:
        stateData = f.read()
        return stateData
