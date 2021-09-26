import unittest
import Gameboard

class Test_TestGameboard(unittest.TestCase):

    """
    Testing Gameboard's getColumnNum function
    """
    # testing normal functionality
    def test_getColumnNum1(self):

        result = Gameboard.getColumnNum("col4")
        assert result == 3

    # testing with column outside of 1-7.
    def test_getColumnNum2(self):
        try:
            result = Gameboard.getColumnNum("col9")
            assert False
        except ValueError:
            assert True

    # testing with incorrect formatting of argument
    def test_getColumnNum3(self):
        try:
            result = Gameboard.getColumnNum("column6")
            assert False
        except ValueError:
            assert True

    # testing with invalid input
    def test_getColumnNum4(self):
        try:
            result = Gameboard.getColumnNum(15)
            assert False
        except TypeError:
            assert True



    """
    
    """



