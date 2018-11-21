# test_creditscalc

import unittest
import api_calls


class TestCreditsCalc(unittest.TestCase):

    def test_getAllClients(self):
        self.assertEqual(None, api_calls.getAllClients())
