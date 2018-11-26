import json
import os
from db import Db

env = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT')
}

db = Db(env)

def get_all_clients():
    sql = "SELECT * from clients"
    data = db.query(sql)
    return json.dumps(data)

def get_client(id):
    sql = f"SELECT * from clients where client_id = {id}"
    data = db.query(sql)
    return json.dumps(data[0])
