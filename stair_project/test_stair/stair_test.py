from stair.striecase import stiarcase

import unittest


class Teststair(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        number = 2
        pattern = '#'
        expected_output = (\
        " #\n" +
        "##")
        # act
        result = stiarcase(number, pattern)
        # assert
        self.assertEqual(result, f'{expected_output}')
