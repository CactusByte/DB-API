from flask import Flask
from flask_cors import CORS

from src.handler.AthleteHandler import AthletesHandler

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/athlete')
def handleAthletes():
    return AthletesHandler().getAllAthletes()

@app.route('/athlete/<athleteId>')
def getAthleteById(athleteId):
    return AthletesHandler().getAthleteById(athleteId)

if __name__ == '__main__':
    app.run(debug=True)


