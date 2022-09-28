from src.catandmouses import cat_and_mouse

import unittest

class Testcatandmouse(unittest.TestCase):
    def test_give_1_2_3_show_cat_B(self):
        line_st = [1,2,3]
        line = map(int,line_st)

        result = cat_and_mouse(*line)
        self.assertEqual(result,'Cat B')
    def test_give_1_3_2_show_mouse_c(self):
        line_st = [1,3,2]
        line = map(int,line_st)

        result = cat_and_mouse(*line)
        self.assertEqual(result,'Mouse C')
    def test_give_3_5_2_show_cat_a(self):
        line_st = [3,5,2]
        line = map(int,line_st)

        result = cat_and_mouse(*line)
        self.assertEqual(result,'Cat A')