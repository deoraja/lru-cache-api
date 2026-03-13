import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

class PostgresDatabase:

    def __init__(self):

        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )

        self.cursor = self.conn.cursor()


    def get(self, key):

        self.cursor.execute(
            "SELECT name FROM Users WHERE id = %s",
            (key,)
        )

        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None