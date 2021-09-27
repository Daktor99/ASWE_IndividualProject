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
        game.makeMove("col1", 'red')

        # checking that move is changed to player 2
        assert game.isValidTurn("p2")

    # testing when it's not the current player's turn
    def test_isValidTurn3(self):

        # initializing game
        game = Gameboard.Gameboard()

        # make sure you're not able to move when not your turn
        assert not game.isValidTurn('p2')

    # testing invalid argument
    def test_isValidTurn4(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            result = game.isValidTurn("p3")
            assert False
        except ValueError:
            assert True

    # testing invalid type
    def test_isValidTurn5(self):

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



    """
    Testing GameBoard's changeTurn function
    """

    # testing normal functionality
    def test_changeTurn1(self):

        # initializing game
        game = Gameboard.Gameboard()

        # changing turn
        game.changeTurn()
        assert game.current_turn == 'p2'

        # changing turn again
        game.changeTurn()
        assert game.current_turn == 'p1'

    # testing invalid functionality
    def test_changeTurn2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # changing current_turn to an invalid value
        try:
            game.current_turn = "bad value"
            game.changeTurn()
            assert False
        except ValueError:
            assert True



    """
    Testing Gameboard's makeMove function
    """

    # testing normal functionality
    def test_makeMove1(self):

        # initializing game
        game = Gameboard.Gameboard()

        # making first move in first column
        game.makeMove("col1", "red")

        # make sure that chip placed in correct spot
        assert game.board[5][0] == "red"
        assert game.remaining_moves == 41
        assert game.current_turn == "p2"

    # testing when column full
    def test_makeMove2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0]]

        try:
            game.makeMove("col1", "red")
            assert False
        except ValueError:
            assert True

    # testing with invalid column
    def test_makeMove3(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            # make move with invalid column
            game.makeMove("col9", "red")
            assert False
        except ValueError:
            assert True

    # testing with invalid player
    def test_makeMove4(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            # make move with invalid player argument
            game.makeMove("col2", "blue")
            assert False
        except ValueError:
            assert True



    """
    Testing Gameboard's checkValidPlayer function
    """

    # testing normal functionality: player is valid
    def test_checkValidPlayer1(self):

        assert Gameboard.checkValidPlayer('red')
        assert Gameboard.checkValidPlayer('yellow')

    # testing normal functionality: player is not valid
    def test_checkValidPlayer2(self):

        assert not Gameboard.checkValidPlayer("blue")

    # testing invalid argument type
    def test_checkValidPlayer3(self):

        try:
            Gameboard.checkValidPlayer(164)
            assert False
        except TypeError:
            assert True



    """
    Testing Gameboard's checkHorizontal function
    """

    # testing normal functionality: horizontal 4 in a row exists
    def test_checkHorizontal1(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column
        game.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['yellow', 'yellow', 'yellow', 0, 0, 0, 0],
                      ['red', 'red', 'yellow', 'red', 'red', 'red', 'red']]

        # check to make sure red won
        assert game.checkHorizontal("red")

    # testing normal functionality: no horizontal 4 in a row exists
    def test_checkHorizontal2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column, no horizontal 4 in a row
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0]]

        # check to make sure neither side has won
        assert not game.checkHorizontal("red")
        assert not game.checkHorizontal("yellow")

    # testing invalid argument being passed
    def test_checkHorizontal3(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column, no horizontal 4 in a row
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0]]

        try:
            game.checkHorizontal("blue")
            assert False
        except ValueError:
            assert True

    # testing invalid type being passed
    def test_checkHorizontal4(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column, no horizontal 4 in a row
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['red', 0, 0, 0, 0, 0, 0]]

        # passing invalid argument to checkHorizontal
        try:
            game.checkHorizontal(246)
            assert False
        except TypeError:
            assert True


    

