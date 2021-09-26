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

    """
    Testing Gameboard's isValidCol function
    """

    # testing regular functionality
    def test_isValidCol1(self):

        # initializing game
        game = Gameboard.Gameboard()

        # board should be clear, check if we can move in first column
        assert game.isValidCol("col1")

    # testing unusual functionality: when a column is full
    def test_isValidCol2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # setting the first column to be full
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0]]

        # make sure we are not able to move on this column
        assert not game.isValidCol("col1")

    # testing invalid column
    def test_isValidCol3(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            game.isValidCol("col9")
            assert False
        except ValueError:
            assert True

    # testing invalid type
    def test_isValidCol4(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            game.isValidCol(13)
            assert False
        except TypeError:
            assert True
