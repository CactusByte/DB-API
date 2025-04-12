from flask import Blueprint
from handler.AthleteHandler import AthletesHandler

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return 'Hello World!'

@routes.route('/athlete', methods=['GET'])
def handleAthletes():
    return AthletesHandler().getAllAthletes()

@routes.route('/athlete', methods=['POST'])
def createAthlete():
    return AthletesHandler().createAthlete()

@routes.route('/athlete/<athleteId>', methods=['GET'])
def getAthleteById(athleteId):
    return AthletesHandler().getAthleteById(athleteId)

@routes.route('/athlete/<athleteId>', methods=['PUT'])
def updateAthlete(athleteId):
    return AthletesHandler().updateAthlete(athleteId)

@routes.route('/athlete/<athleteId>', methods=['DELETE'])
def deleteAthlete(athleteId):
    return AthletesHandler().deleteAthlete(athleteId)