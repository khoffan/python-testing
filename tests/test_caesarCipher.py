from src.caesarCipher import caesarCipher

import unittest

class TestCeasarCipher(unittest.TestCase):
    def test_ceasarforword_2_charector(self):
        s = 'Middle-of-destiny'
        number = 2
        expect = 'Okffng-qh-fguvkpa'

        result = caesarCipher(s, number)

        self.assertEqual(expect, result)
    def test_ceasarforword_3_charector(self):
        s = 'Oasis-in-maddness'
        number = 3
        expect = 'Rdvlv-lq-pdggqhvv'

        result = caesarCipher(s, number)

        self.assertEqual(expect, result)
    def test_ceasarforword_4_charector(self):
        s = 'Power-to-yourself'
        number = 4
        expect = 'Tsaiv-xs-csyvwipj'

        result = caesarCipher(s, number)

        self.assertEqual(expect, result)
    def test_ceasarforword_2_charector_no_string(self):
        s = ''
        number = 2
        expect = 'Tsaiv-xs-csyvwipj'

        result = caesarCipher(s, number)

        self.assertNotEqual(result, expect)
    def test_ceasarforword_101_charector(self):
        s = 'Middle-of-destiny'
        number = 101
        expect = 'Okffng-qh-fguvkpa'

        result = caesarCipher(s, number)

        self.assertNotEqual(result, expect)
    def test_ceasarforword_101_charector_no_string(self):
        s = 'abcdefghijklmnopqrstuvwxyz'
        number = -1
        expect = 'zabcdefghijklmnopqrstuvwxy'

        result = caesarCipher(s, number)

        self.assertEqual(expect, result)