import json
from flask_restful import Resource
from db import Db

class ClientList(Resource):
    def __init__(self):
        self.db = Db()

    def get(self):
        sql = "SELECT * from clients"
        data = self.db.query(sql)
        return data, 200

class Client(Resource):
    def __init__(self):
        self.db = Db()

    def get(self, id):
        sql = f"SELECT * from clients where id = {id}"
        data = self.db.query(sql)
        return data, 200

