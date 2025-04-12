import psycopg2
from config.dbconfig import pg_config
from models.AthleteModel import Athlete

class AthleteDAO:
    def __init__(self):
        url = "dbname = %s password = %s host = %s port = %s user= %s" % \
              (pg_config['database'],
               pg_config['password'],
               pg_config['host'],
               pg_config['port'],
               pg_config['user']
               )

        self.conn = psycopg2.connect(url)

    def getAllAthletes(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM athletes"
        cursor.execute(query)
        athletes = []
        for row in cursor:
            athlete = Athlete(
                id=row[0],
                name=row[1],
                age=row[2],
                gender=row[3],
                height=row[4],
                weight=row[5]
            )
            athletes.append(athlete)
        cursor.close()
        return athletes

    def getAthleteById(self, athlete_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM athletes WHERE id = %s"
        cursor.execute(query, (athlete_id,))
        row = cursor.fetchone()
        if row:
            athlete = Athlete(
                id=row[0],
                name=row[1],
                age=row[2],
                gender=row[3],
                height=row[4],
                weight=row[5]
            )
            return athlete
        return None

    def createAthlete(self, athlete):
        cursor = self.conn.cursor()
        query = "INSERT INTO athletes (name, age, gender, height, weight) VALUES (%s, %s, %s, %s, %s) RETURNING id"
        cursor.execute(query, (athlete.name, athlete.age, athlete.gender, athlete.height, athlete.weight))
        athlete_id = cursor.fetchone()[0]
        self.conn.commit()
        cursor.close()
        return athlete_id

    def updateAthlete(self, athlete):
        cursor = self.conn.cursor()
        query = "UPDATE athletes SET name = %s, age = %s, gender = %s, height = %s, weight = %s WHERE id = %s"
        cursor.execute(query, (athlete.name, athlete.age, athlete.gender, athlete.height, athlete.weight, athlete.id))
        rows_affected = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return rows_affected > 0

    def deleteAthlete(self, athlete_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM athletes WHERE id = %s"
        cursor.execute(query, (athlete_id,))
        rows_affected = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return rows_affected > 0
