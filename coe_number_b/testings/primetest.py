
from coe_number.number_units import is_prime_list

import unittest

class TestPrime(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        number = [1,2,3]
        prime_num = is_prime_list(number)
        self.assertTrue(prime_num)
    def test_give_4_5_6_is_prime(self):
        number = [4,5,6]
        prime_num = is_prime_list(number)
        self.assertFalse(prime_num)
    def test_give_7_8_9_is_prime(self):
        number = [7,8,9]
        prime_num = is_prime_list(number)
        self.assertFalse(prime_num)
    def test_give_10_11_12_is_prime(self):
        number = [10,11,12]
        prime_num = is_prime_list(number)
        self.assertFalse(prime_num) 
    def test_give_13_14_15_is_prime(self):
        number = [13,14,15]
        prime_num = is_prime_list(number)
        self.assertFalse(prime_num)
    def test_give_16_17_18_is_prime(self):
        number = [16,17,18]
        prime_num = is_prime_list(number)
        self.assertFalse(prime_num)