import psycopg2
import json

def getAllClients():
    allClients = []
    sql = "SELECT * from clients"
    conn = psycopg2.connect('dbname=evolveu')
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
        allClients.append({'id': row[0], 'name': row[1]})

    cur.close()
    conn.close()

    print(allClients)

    return json.dumps(allClients)


def getClient(id):
    allClients = []
    sql = "SELECT * from clients where id = id"
    conn = psycopg2.connect('dbname=evolveu')
    cur = conn.cursor()
    cur.execute(sql)

    row = cur.fetchone()
    cur.close()
    conn.close()

    print({'id': row[0], 'name': row[1]})

    return json.dumps([{'id': row[0], 'name': row[1]}])

