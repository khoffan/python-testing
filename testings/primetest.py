
from code_project.prime_list import is_prime_list


import unittest

class TestPrime(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        # list number assertTrue
        number = [1,2,3]
        prime_num = is_prime_list(number)
        self.assertTrue(prime_num) 

if __name__ == '__main__':
    unittest.main()