# testing API calls

import unittest
import api_calls


class TestCreditsCalc(unittest.TestCase):

    def test_getAllClients(self):
        should_be = '[{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}, {"id": 3, "name": "Next Client"}, {"id": 4, "name": "Previous Client"}, {"id": 5, "name": "Super Client"}]'
        self.assertEqual(should_be, api_calls.getAllClients())

    def test_getClient(self):
        should_be = '[{"id": 1, "name": "John Doe"}]'
        self.assertEqual(should_be, api_calls.getClient(1))
