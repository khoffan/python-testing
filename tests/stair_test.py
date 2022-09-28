from src.striecase import stiarcase

import unittest


class Teststair(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        number = 2 ; pattern = '#'
        expected_output = [
        ' #',
        '##'
        ]
        # act
        result = stiarcase(number, pattern)
        # assert
        self.assertEqual(result,expected_output)
    def test_give_3_with_hash_should_be_hh(self):
        number = 3 ; pattern = '#'
        expected_output = [
        '  #',
        ' ##',
        '###'
        ]
        # act
        result = stiarcase(number, pattern)
        # assert
        self.assertEqual(result,expected_output)
    def test_give_0_with_hash_should_be(self):
        number = 0 ; pattern = '#'
        expected_output = []
        # act
        result = stiarcase(number, pattern)
        # assert
        self.assertEqual(result,expected_output)
    def test_give_5_with_hash_should_be(self):
        number = 5 ; pattern = '#'
        expected_output = [
            '    #',
            '   ##',
            '  ###',
            ' ####',
            '#####'
            
        ]
        # act
        result = stiarcase(number, pattern)
        # assert
        self.assertEqual(result,expected_output)
    def test_give_31_with_hash_should_be(self):
        number = 31 ; pattern = '#'
        expected_output = []
        # act
        result = stiarcase(number, pattern)
        # assert
        self.assertEqual(result,expected_output)
