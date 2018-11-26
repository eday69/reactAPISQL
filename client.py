from flask_restful import Resource
import psycopg2

class ClientList(Resource):
    def get(self):
        sql = "SELECT * from clients"


        conn = psycopg2.connect('dbname=evolveu')
        cur = conn.cursor()
        cur.execute(sql)

        clients = []
        rows = cur.fetchall()
        for row in rows:
            clients.append({'id': row[0], 'name': row[1]})

        cur.close()
        conn.close()

        return {'clients': clients}
