# -*- coding: utf-8 -*-

import unittest
from main import print_numbers, is_multiple_of_x


class TestMainModule(unittest.TestCase):

    def test_is_multiple_of_x(self):
        self.assertTrue(is_multiple_of_x(5, 5))
        self.assertTrue(is_multiple_of_x(15, 5))
        self.assertTrue(is_multiple_of_x(15, 3))
        self.assertFalse(is_multiple_of_x(15, 7))
        self.assertTrue(is_multiple_of_x(9, 3))

    def test_print_numbers(self):
        self.assertEqual(print_numbers(3), 'Three')
        self.assertEqual(print_numbers(5), 'Five')
        self.assertEqual(print_numbers(15), 'ThreeFive')
        self.assertEqual(print_numbers(16), '16')
        self.assertEqual(print_numbers(101), 'Value out of bound!!')        
        self.assertEqual(print_numbers(-1), 'Value out of bound!!')        

       

if __name__ == "__main__":
    unittest.main()
