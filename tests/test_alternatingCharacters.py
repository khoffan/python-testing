from src.alternatingCharacters import alternatingCharacters

import unittest

class TestalternatingCharacters(unittest.TestCase):
    def test_alternatingCharacters_AAAAA_in_3(self):
        s = 'AAAA'
        expact = 3

        result = alternatingCharacters(s)

        self.assertEqual(result,expact)
    def test_alternatingCharacters_ABABABAB_in_0(self):
        s = 'ABABABAB'
        expact = 0

        result = alternatingCharacters(s)

        self.assertEqual(result,expact)
    def test_alternatingCharacters_AAABBB_in_4(self):
        s = 'AAABBB'
        expact = 4

        result = alternatingCharacters(s)

        self.assertEqual(result,expact)
    def test_alternatingCharacters_AAABBB_not_4(self):
        s = 'AAABBB'
        expact = 3

        result = alternatingCharacters(s)

        self.assertNotEqual(result,expact)