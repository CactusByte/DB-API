import psycopg2
from src.config.dbconfig import pg_config
from src.models.AthleteModel import Athlete

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
