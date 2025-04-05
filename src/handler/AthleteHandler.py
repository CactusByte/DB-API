from flask import jsonify
from src.DAO.AthleteDAO import AthleteDAO

class AthletesHandler:
    def getAllAthletes(self):
        dao = AthleteDAO()
        # Assume that getAllAthletes returns a list of Athlete objects.
        athletes = dao.getAllAthletes()
        athletesList = []

        for athlete in athletes:
            athlete = athlete.to_dict()
            athletesList.append(athlete)

        return jsonify(athletesList)

    def getAthleteById(self, athleteId):
        dao = AthleteDAO()
        athlete = dao.getAthleteById(athleteId)
        if athlete:
            return jsonify(athlete.to_dict()), 200
        else:
            return jsonify({"error": "Athlete not found"}), 404


