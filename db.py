import psycopg2
import json
import os

env = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT')
}

class Db:
    def __init__(self):
        global env
        self._connection_values = env 
        self._connection = None

    @classmethod
    def init_test_db(self):
        self.connect()
        with self._connection as cursor:
            cursor.execute(open("generate_test_db.sql", "r").read())
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = psycopg2.connect(**self._connection_values)
            print("You have been connected to the db.")
        else:
            print("The connection already exists.")

    def disconnect(self):
        self._connection.close()
        print("The connection has been closed.")

    # default query function to make a db call
    def query(self, queryString):
        print(queryString)
        self.connect()
        cur = self._connection.cursor()

        cur.execute(queryString)
        self._connection.commit()

        column_array = [desc[0] for desc in cur.description]

        rows = cur.fetchall()
        cur.close()
        self.disconnect()

        data = []
        for row in rows:
            obj = {}
            for column in range(0, len(column_array)):
                obj[column_array[column]] =  row[column]
            data.append(obj)

        return data
