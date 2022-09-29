from src.gridChallenge import gridChallenge

import unittest

class TestgridChallenge(unittest.TestCase):
    def test_gride_of_3_by_3(self):
        grids_lt = ['abc','ade','cdf']

        result = gridChallenge(grids_lt)
        self.assertTrue(result)

    def test_gride_False(self):
        grids_lt = ['abck','adeg','cdfu']

        result = gridChallenge(grids_lt)
        self.assertFalse(result)

    def test_gride_of_5_by_5(self):
        grids_lt = ['vpvv','pvvv','vzzp','zzyy']

        result = gridChallenge(grids_lt)
        self.assertTrue(result)
        
    def test_gride_over_length(self):
        grids_lt = ['vpvv']*101

        result = gridChallenge(grids_lt)
        self.assertIsNone(result)