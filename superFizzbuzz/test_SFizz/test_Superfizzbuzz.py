from src.Sufizzbuzz import show_fizzbuzz

import unittest

class testsuperfizzbuzz(unittest.TestCase):
    def get_fizz_to_number_of_3(self):
        number = 3
        result = show_fizzbuzz(number)
        self.assertEquals(result,'Fizz')
    # def get_fizz_number_3(self):
    #     number = 3
    #     result = superFizzBuzz(number)
    #     self.assertEqual(result,'Fizz')
    # def get_fizz_number_5(self):
    #     number = 5
    #     result = superFizzBuzz(number)
    #     self.assertEqual(result,'Buzz')
    # def get_fizz_number_9(self):
    #     number = 9
    #     result = superFizzBuzz(number)
    #     self.assertEqual(result,'FizzFizz')
    # def get_fizz_number_25(self):
    #     number = 25
    #     result = superFizzBuzz(number)
    #     self.assertEqual(result,'BuzzBuzz')
    # def get_fizz_number_15(self):
    #     number = 15
    #     result = superFizzBuzz(number)
    #     self.assertEqual(result,'FizzBuzz')
    # def get_fizz_number_50(self):
    #     number = 50;
    #     result = superFizzBuzz(number)
    #     self.assertEqual(result,'NoFizzBuzz')
    # def get_fizz_number_9(self):
    #     number = 3;
    #     result = superFizzBuzz(number)
    #     self.assertEqual(result,'Fizz')