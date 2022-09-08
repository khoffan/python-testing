from src.Sufizzbuzz import show_fizzbuzz

import unittest

class testsuperfizzbuzz(unittest.TestCase):
    def test_fizz_to_number_of_3(self):
        number = 3
        result = show_fizzbuzz(number)
        self.assertEquals(result,'Fizz')
    def test_NO_fizz_to_number_of_2(self):
        number = 2
        result = show_fizzbuzz(number)
        self.assertEquals(result,'NoFizzBuzz')
    def test_Buzz_to_number_of_5(self):
        number = 5
        result = show_fizzbuzz(number)
        self.assertEquals(result,'Buzz')
    def test_fizzBuzz_to_number_of_15(self):
        number = 15
        result = show_fizzbuzz(number)
        self.assertEquals(result,'FizzBuzz')
    def test_FizzFizz_to_number_of_18(self):
        number = 9
        result = show_fizzbuzz(number)
        self.assertEquals(result,'FizzFizz')
    def test_BuzzBuzz_to_number_of_50(self):
        number = 50
        result = show_fizzbuzz(number)
        self.assertEquals(result,'BuzzBuzz')
    def test_FizzFizzBuzzBuzz_number_4725(self):
        number = 225
        result = show_fizzbuzz(number)
        self.assertEqual(result,'FizzFizzBuzzBuzz')
    def test_Not_FizzFizzBuzzBuzz_number_4725(self):
        number = 224
        result = show_fizzbuzz(number)
        self.assertNotEqual(result,'FizzFizzBuzzBuzz')
    def test_NofizzBuzz_number_1(self):
        number = 1
        result = show_fizzbuzz(number)
        self.assertEqual(result,'NoFizzBuzz')
   