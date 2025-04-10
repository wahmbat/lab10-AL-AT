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


    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()