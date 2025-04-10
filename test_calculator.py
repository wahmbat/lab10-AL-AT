#https://github.com/wahmbat/lab10-AL-AT.git
#Partner 1: Alan Lin
#Partner 2: Anjali Tomerlin

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(1,1),2)
        self.assertEqual(add(-4,0),-4)
        self.assertEqual(add(-4,-5),-9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1,1),0)
        self.assertEqual(subtract(-1,-1),-2)
        self.assertEqual(subtract(-3,4),1)


    def test_multiply(self):
        test1 = mul(3,5)
        expected1 = 15
        self.assertEqual(test1, expected1)

        test2 = mul(7,2)
        expected2 = 14
        self.assertEqual(test2, expected2)

        test3 = mul(17,23)
        expected3 = 391
        self.assertEqual(test3, expected3)

    def test_divide(self):
        test1 = div(3,15)
        expected1 = 5
        self.assertEqual(test1, expected1)

        test2 = div(24,12)
        expected2 = 0.5
        self.assertEqual(test2, expected2)

        test3 = div(3,18)
        expected3 = 6
        self.assertEqual(test3, expected3)
    # ##########################


    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(DivideByZeroError):
            div(5,0)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,4),2)
        self.assertEqual(logarithm(3,10), 2.09590327)
        self.assertEqual(logarithm(2,1),0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1,0)
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        test1 = hypotenuse(3,4)
        expected1 = 5.0
        self.assertEqual(test1, expected1)

        test2 = hypotenuse(3,3)
        expected2 = 4.24264068
        self.assertAlmostEquals(test2, expected2)

        test3 = hypotenuse(7,12)
        expected3 = 13.89244398
        self.assertAlmostEquals(test3, expected3)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-3)

        test1 = square_root(4)
        expected1 = 2.0
        self.assertEqual(test1, expected1)

        test2 = square_root(64)
        expected2 = 8.0
        self.assertEqual(test2, expected2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
