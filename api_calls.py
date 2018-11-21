import psycopg2

def getAllClients():
    allClients = []
    sql = "SELECT * from clients"
    conn = psycopg2.connect('dbname=evolveu')
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
        allClients.append([row[0], row[1]])

    cur.close()
    conn.close()

    return json.dumps(**allClients)
