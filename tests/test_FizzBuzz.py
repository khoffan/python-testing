from src.FizzBuzz import get_fizzbizz

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_get_fizzbizz_1(self):
        num = 1
        self.assertNotEqual(get_fizzbizz(num), 1)
    def test_get_fizzbizz_3(self):
        num = 3
        self.assertEqual(get_fizzbizz(num), 'Fizz')
    def test_get_fizzbizz_5(self):
        num = 5
        self.assertEqual(get_fizzbizz(num), 'Buzz')
    def test_get_fizzbizz_15(self):
        num = 15
        self.assertEqual(get_fizzbizz(num), 'FizzBuzz')