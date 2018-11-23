# testing API calls

import unittest
import api_calls


class TestCreditsCalc(unittest.TestCase):

    def test_getAllClients(self):
        should_be = '[{"id": 1, "name": "Eric Day"}, {"id": 2, "name": "Tish Day"}]'
        self.assertEqual(should_be, api_calls.getAllClients())
