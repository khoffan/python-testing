from src.ex_one import funnyString

import unittest

class testFunnyString(unittest.TestCase):
    def test_Not_Funny_string_naruzami(self):
        s = 'naruzami'
        expect = 'Not Funny'

        result = funnyString(s)
        self.assertEqual(result,expect)

    def test_Not_Funny_string_bcxz(self):
        s = 'bcxz'
        expect = 'Not Funny'

        result = funnyString(s)

        self.assertEqual(result,expect)

    def test_Funny_string_acxz(self):
        s = 'acxz'
        expect = 'Funny'

        result = funnyString(s)

        self.assertEqual(result,expect)
