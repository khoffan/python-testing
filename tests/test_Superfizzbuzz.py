from src.Sufizzbuzz import super_fizzbuzz

import unittest

class testsuperfizzbuzz(unittest.TestCase):
    def test_fizz_to_number_of_3(self):
        number = 3
        expeact = 'Fizz'
        result = super_fizzbuzz(number)
        self.assertEquals(result, expeact)
    def test_NO_fizz_to_number_of_2(self):
        number = 2
        expeact = 'NoFizzBuzz'
        result = super_fizzbuzz(number)
        self.assertEquals(result, expeact)
    def test_Buzz_to_number_of_25(self):
        number = 5
        expeact = 'Buzz'
        result = super_fizzbuzz(number)
        self.assertEquals(result, expeact)
    def test_fizzBuzz_to_number_of_15(self):
        number = 15
        expeact = 'FizzBuzz'
        result = super_fizzbuzz(number)
        self.assertEquals(result, expeact)
    def test_BuzzBuzz_to_number_of_25(self):
        number = 25
        expeact = 'BuzzBuzz'
        result = super_fizzbuzz(number)
        self.assertEquals(result, expeact)
    def test_NofizzBuzz_number_1(self):
        number = 1
        expeact = 'NoFizzBuzz'
        result = super_fizzbuzz(number)
        self.assertEqual(result, expeact)
    def test_NofizzBuzz_number_10001(self):
        number = 10001
        expeact = 'NoFizzBuzz'
        result = super_fizzbuzz(number)
        self.assertEqual(result, expeact)
    def test_BuzzBuzz_number_10000(self):
        number = 10000
        expeact = 'BuzzBuzz'
        result = super_fizzbuzz(number)
        self.assertEqual(result, expeact)
    def test_BuzzBuzz_number_5000(self):
        number = 5000
        expeact = 'BuzzBuzz'
        result = super_fizzbuzz(number)
        self.assertEqual(result, expeact)
    def test_Buzz_number_9356(self):
        number = 9355
        expeact = 'Buzz'
        result = super_fizzbuzz(number)
        self.assertEqual(result, expeact)
    def test_Fizz_number_9356(self):
        number = 2499
        expeact = 'Fizz'
        result = super_fizzbuzz(number)
        self.assertEqual(result, expeact)
    def test_fizz_number_9356(self):
        number = 5568
        expeact = 'Fizz'
        result = super_fizzbuzz(number)
        self.assertEqual(result, expeact)
    def test_BuzzBuzz_number_9356(self):
        number = 7000
        expeact = 'BuzzBuzz'
        result = super_fizzbuzz(number)
        self.assertEqual(result, expeact)
    def test_give_135_return_fizzfizz(self):
        num = 135
        expect = 'FizzFizz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    def test_give_6075_return_fizzfizzbuzzbuzz(self):
        num = 6075
        expect = 'FizzFizzBuzzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
   