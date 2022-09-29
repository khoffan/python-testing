from src.two_charector import alternate

import unittest

class TestTwocharector(unittest.TestCase):
    def test_two_charector_of_5(self):
        s = 'beabeefeab'
        expect = 5

        result = alternate(s)

        self.assertEqual(result, expect)

    def test_two_charector_of_4(self):
        s = 'gege'
        expect = 4

        result = alternate(s)

        self.assertEqual(result, expect)

    def test_two_charector_of_6(self):
        s = 'ghijfghtgdhsdsea'
        expect = 6

        result = alternate(s)

        self.assertEqual(result, expect)
        
    def test_two_charector_by_strimg_over_1000(self):
        s = 'abhgba'*1000
        expect = -1

        result = alternate(s)

        self.assertEqual(result, expect)