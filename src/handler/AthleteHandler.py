from flask import jsonify, request
from DAO.AthleteDAO import AthleteDAO
from models.AthleteModel import Athlete

class AthletesHandler:
    def getAllAthletes(self):
        dao = AthleteDAO()

        athletes = dao.getAllAthletes()
        athletesList = []

        for athlete in athletes:
            athlete = athlete.to_dict()
            athletesList.append(athlete)

        return jsonify(athletesList), 200

    def getAthleteById(self, athleteId):
        dao = AthleteDAO()
        athlete = dao.getAthleteById(athleteId)
        if athlete:
            return jsonify(athlete.to_dict()), 200
        else:
            return jsonify({"error": "Athlete not found"}), 404

    def createAthlete(self):
        dao = AthleteDAO()
        data = request.get_json()
        
        required_fields = ['name', 'age', 'gender', 'height', 'weight']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
                
        athlete = Athlete(
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            height=data['height'],
            weight=data['weight']
        )
        
        athlete_id = dao.createAthlete(athlete)

        athlete.id = athlete_id
        return jsonify(athlete.to_dict()), 201

    def updateAthlete(self, athleteId):
        dao = AthleteDAO()
        data = request.get_json()
        
        existing_athlete = dao.getAthleteById(athleteId)
        if not existing_athlete:
            return jsonify({"error": "Athlete not found"}), 404
            
        required_fields = ['name', 'age', 'gender', 'height', 'weight']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
                
        updated_athlete = Athlete(
            id=athleteId,
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            height=data['height'],
            weight=data['weight']
        )
        
        success = dao.updateAthlete(updated_athlete)
        
        if success:
            return jsonify("Updated athlete object."), 200
        else:
            return jsonify({"error": "Failed to update athlete"}), 500

    def deleteAthlete(self, athleteId):
        dao = AthleteDAO()
        
        existing_athlete = dao.getAthleteById(athleteId)
        if not existing_athlete:
            return jsonify({"error": "Athlete not found"}), 404
            
        success = dao.deleteAthlete(athleteId)
        
        if success:
            return '', 204
        else:
            return jsonify({"error": "Failed to delete athlete"}), 500


