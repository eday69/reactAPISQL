# testing API calls

import unittest
from db import Db


class TestDb(unittest.TestCase):
    def setUp(self):
        db = Db()
        db.connect()

    def tearDown(self):
        db.disconnect()

    def test_init_test_db(self):
        Db().init_test_db()
        should_be = '[{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}, {"id": 3, "name": "Next Client"}, {"id": 4, "name": "Previous Client"}, {"id": 5, "name": "Super Client"}]'
        self.assertEqual(should_be, api_calls.getAllClients())

    def test_query(self):
        pass

