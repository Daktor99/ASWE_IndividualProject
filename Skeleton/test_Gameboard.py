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
    Testing Gameboard's isValidTurn function 
    """

    # testing normal functionality
    def test_isValidTurn1(self):

        # initializing game
        game = Gameboard.Gameboard()

        # checking to make sure that the first turn is player 1
        assert game.isValidTurn("p1")

    # testing normal functionality after making a move
    def test_isValidTurn2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # making move to change turn
        game.makeMove("col1", "p1")

        # checking that move is changed to player 2
        assert game.isValidTurn("p2")

    # testing invalid argument
    def test_isValidTurn3(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            result = game.isValidTurn("p3")
            assert False
        except ValueError:
            assert True

    # testing invalid type
    def test_isValidTurn4(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            result = game.isValidTurn(13)
            assert False
        except TypeError:
            assert True





