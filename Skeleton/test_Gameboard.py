import unittest
import Gameboard
from unittest.mock import patch


class Test_TestGameboard(unittest.TestCase):
    """
    Testing Gameboard's getColumnNum function
    """

    # testing normal functionality: column selected within bounds
    def test_getColumnNum1(self):

        result = Gameboard.getColumnNum("col4")
        assert result == 3

    # testing with column outside of 1-7.
    def test_getColumnNum2(self):
        try:
            Gameboard.getColumnNum("col9")
            assert False
        except ValueError:
            assert True

    # testing with incorrect formatting of argument
    def test_getColumnNum3(self):
        try:
            Gameboard.getColumnNum("column6")
            assert False
        except ValueError:
            assert True

    # testing with invalid input
    def test_getColumnNum4(self):
        try:
            Gameboard.getColumnNum(15)
            assert False
        except TypeError:
            assert True

    """
    Testing Gameboard's isValidTurn function
    """

    # testing normal functionality: it is the current player's turn
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
        game.makeMove('col1', 'p1', "red")

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
            game.isValidTurn("p3")
            assert False
        except ValueError:
            assert True

    # testing invalid type
    def test_isValidTurn5(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            game.isValidTurn(13)
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
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0]]

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
        game.makeMove("col1", 'p1', "red")

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
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0]]

        try:
            game.makeMove('col1', 'p1', "red")
            assert False
        except ValueError:
            assert True

    # testing with invalid column
    def test_makeMove3(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            # make move with invalid column
            game.makeMove('col9', 'p1', "red")
            assert False
        except ValueError:
            assert True

    # testing with invalid playerColor
    def test_makeMove4(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            # make move with invalid playerColor argument
            game.makeMove('col2', 'p1', 'blue')
            assert False
        except ValueError:
            assert True

    # testing with invalid player turn
    def test_makeMove5(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            # make move with invalid playerColor argument
            game.makeMove('col2', 'p2', "red")
            assert False
        except ValueError:
            assert True

    # testing when the game has no move available moves to be made
    def test_makeMove6(self):

        # initializing game & reducing remaining moves to 0
        game = Gameboard.Gameboard()
        game.remaining_moves = 0

        try:
            # make move with invalid playerColor argument
            game.makeMove('col2', 'p1', "red")
            assert False
        except ValueError:
            assert True

    # testing when the game already has a winner
    def test_makeMove7(self):

        # initializing game
        game = Gameboard.Gameboard()
        game.game_result = 'p1'

        try:
            # try to make a move with winner
            game.makeMove('col1', 'p1', "red")
            assert False
        except ValueError:
            assert True

    """
    Testing Gameboard's checkValidPlayer function
    """

    # testing normal functionality: player is valid
    def test_checkValidPlayer1(self):

        assert Gameboard.checkValidPlayer("red")
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

        # making red have 4 in a row
        game.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['yellow', 'yellow', 'yellow', 0, 0, 0, 0],
                      ["red", "red", 'yellow', "red", "red", "red", "red"]]

        # check to make sure red won
        assert game.checkHorizontal("red")
        # check to make sure yellow doesn't have winning state either
        assert not game.checkVertical("yellow")

    # testing normal functionality: no horizontal 4 in a row exists
    def test_checkHorizontal2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column, no horizontal 4 in a row
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0]]

        # check to make sure neither side has won
        assert not game.checkHorizontal("red")
        assert not game.checkHorizontal("yellow")

    # testing invalid argument being passed
    def test_checkHorizontal3(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column, no horizontal 4 in a row
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0]]

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
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0]]

        # passing invalid argument to checkHorizontal
        try:
            game.checkHorizontal(246)
            assert False
        except TypeError:
            assert True

    """
    Testing Gameboard's checkVertical
    """

    # testing normal functionality: vertical win exists
    def test_checkVertical1(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column with vertical 4 in a row
        game.board = [["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 'yellow', 0, 0, 0, 0, 0],
                      ["red", 'yellow', 'yellow', 0, 0, 0, 0]]

        # check to make sure that vertical win is detected
        assert game.checkVertical("red")
        # check to make sure that yellow doesn't have vertical 4 in a row
        assert not game.checkVertical("yellow")

    # testing normal functionality: no vertical 4 in a row
    def test_checkVertical2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column, no vertical 4 in a row
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 'yellow'],
                      ["red", 0, 0, 0, 0, 0, "red"]]

        # making sure that no one won
        assert not game.checkVertical("red")
        assert not game.checkVertical("yellow")

    # testing invalid color argument passed
    def test_checkVertical3(self):

        game = Gameboard.Gameboard()

        # filling up first column with vertical 4 in a row
        game.board = [["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 'yellow', 0, 0, 0, 0, 0],
                      ["red", 'yellow', 'yellow', 0, 0, 0, 0]]

        try:
            game.checkVertical("blue")
            assert False
        except ValueError:
            assert True

    # testing invalid type passed
    def test_checkVertical4(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column with vertical 4 in a row
        game.board = [["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 'yellow', 0, 0, 0, 0, 0],
                      ["red", 'yellow', 'yellow', 0, 0, 0, 0]]

        try:
            game.checkVertical(13)
            assert False
        except TypeError:
            assert True

    """
    Testing Gameboard's checkDiagonal function
    """

    # testing normal functionality: diagonal exists in \ direction
    def test_checkDiagonal1(self):

        # initializing game object
        game = Gameboard.Gameboard()

        # filling up first column with diagonal \ 4 in a row
        game.board = [["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 'yellow', 0, 0, 0, 0, 0],
                      ["red", "red", 'yellow', 0, 0, 0, 0],
                      ["red", 'yellow', 'yellow', 'yellow', 0, 0, 0]]

        assert game.checkDiagonal("yellow")
        assert not game.checkDiagonal("red")

    # testing normal functionality: diagonal exists in / direction
    def test_checkDiagonal2(self):

        # initializing game object
        game = Gameboard.Gameboard()

        # filling up first column with diagonal / 4 in a row
        game.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 'yellow'],
                      [0, 0, 0, 0, 0, 'yellow', "red"],
                      [0, 0, 0, 0, 'yellow', 'yellow', "red"],
                      [0, 0, 0, 'yellow', "red", "red", "red"]]

        assert game.checkDiagonal("yellow")
        assert not game.checkDiagonal("red")

    # testing no diagonal win exists
    def test_checkDiagonal3(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column, no diagonal 4 in a row
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0]]

        assert not game.checkDiagonal("yellow")
        assert not game.checkDiagonal("red")

    # testing invalid argument passed
    def test_checkDiagonal4(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column with diagonal / 4 in a row
        game.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 'yellow'],
                      [0, 0, 0, 0, 0, 'yellow', "red"],
                      [0, 0, 0, 0, 'yellow', 'yellow', "red"],
                      [0, 0, 0, 'yellow', "red", "red", "red"]]

        # try calling function with invalid player color
        try:
            game.checkDiagonal("blue")
            assert False
        except ValueError:
            assert True

    # testing invalid type passed to function
    def test_checkDiagonal5(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            game.checkDiagonal(13)
            assert False
        except TypeError:
            assert True

    """
    Testing Gameboard's checkIfWon function
    """

    # testing with normal functionality: red player wins vertically
    def test_checkIfWon1(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column with vertical 4 in a row
        game.board = [["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 'yellow', 0, 0, 0, 0, 0],
                      ["red", 'yellow', 'yellow', 0, 0, 0, 0]]

        assert game.checkIfWon("red")
        assert not game.checkIfWon("yellow")

    # testing with normal functionality: red player wins horizontally
    def test_checkIfWon2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # making red have 4 in a row
        game.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ['yellow', 'yellow', 'yellow', 0, 0, 0, 0],
                      ["red", "red", 'yellow', "red", "red", "red", "red"]]

        assert game.checkIfWon("red")
        assert not game.checkIfWon("yellow")

    # testing with normal functionality: yellow player wins diagonally
    def test_checkIfWon3(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column with diagonal \ 4 in a row
        game.board = [["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 'yellow', 0, 0, 0, 0, 0],
                      ["red", "red", 'yellow', 0, 0, 0, 0],
                      ["red", 'yellow', 'yellow', 'yellow', 0, 0, 0]]

        assert game.checkIfWon("yellow")
        assert not game.checkIfWon("red")

    # testing normal functionality: no player wins
    def test_checkIfWon4(self):

        # initializing game
        game = Gameboard.Gameboard()

        # filling up first column with vertical 4 in a row
        game.board = [[0, 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 'yellow', 0, 0, 0, 0, 0],
                      ["red", 'yellow', 'yellow', 0, 0, 0, 0]]

        assert not game.checkIfWon("red")
        assert not game.checkIfWon("yellow")

    # testing invalid player color passed
    def test_checkIfWon5(self):

        # initializing game
        game = Gameboard.Gameboard()

        # checkIfWon with "blue" as invalid argument
        try:
            game.checkIfWon("blue")
            assert False
        except ValueError:
            assert True

    # testing invalid type passed as parameter
    def test_checkIfWon6(self):

        # initializing game
        game = Gameboard.Gameboard()

        # checkIfWon with "blue" as invalid argument
        try:
            game.checkIfWon(13)
            assert False
        except TypeError:
            assert True

    """
    Testing Gameboard's setColors function
    """

    # regular usage: player1 is 'red'
    def test_setP1Color1(self):

        # initializing game
        game = Gameboard.Gameboard()

        # checking to see if we set correct colors
        game.setP1Color('red')
        assert game.player1 == 'red'
        assert game.player2 == 'yellow'

    # irregular argument being passed 'blue
    def test_setP1Colors2(self):

        # initializing game
        game = Gameboard.Gameboard()

        # checking to make sure that we get a ValueError
        try:
            game.setP1Color('blue')
            assert False
        except ValueError:
            assert True

    # passing invalid argument type
    def test_setP1Colors3(self):

        # initializing game
        game = Gameboard.Gameboard()

        # checking to make sure that we get a ValueError
        try:
            game.setP1Color(13)
            assert False
        except TypeError:
            assert True

    """
    Testing Gameboard's getP2Color function
    """

    # testing regular functionality
    def test_getP2Color1(self):

        # initializing game
        game = Gameboard.Gameboard()

        game.setP1Color('red')
        assert game.getP2Color() == 'yellow'

        game.setP1Color('yellow')
        assert game.getP2Color() == 'red'

    # testing when p1 has not picked color
    def test_getP2Color2(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            game.getP2Color()
            assert False
        except ValueError:
            assert True

    # testing when p1 color has incorrect value such as blue
    def test_getP2Color3(self):

        # initializing game
        game = Gameboard.Gameboard()

        try:
            game.player2 = 'blue'
            game.getP2Color()
            assert False
        except ValueError:
            assert True

    """
    Testing Gameboard's get_move function
    """

    # testing regular functionality
    def test_getMove1(self):

        # initializing game
        game = Gameboard.Gameboard()
        move = game.getMove()

        assert move[0] == game.current_turn
        assert move[1] == str(game.board)
        assert move[2] == game.game_result
        assert move[3] == game.player1
        assert move[4] == game.player2
        assert move[5] == game.remaining_moves

    # testing getMove on non-initial state
    def test_getMove2(self):

        # initializing gameboard
        game = Gameboard.Gameboard()

        # setting gameboard instances:
        game.board = [['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0],
                      ['yellow', 0, 0, 0, 0, 0, 0],
                      ["red", 0, 0, 0, 0, 0, 0]]
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.remaining_moves = 36

        move = game.getMove()

        assert move[0] == game.current_turn
        assert move[1] == str(game.board)
        assert move[2] == game.game_result
        assert move[3] == game.player1
        assert move[4] == game.player2
        assert move[5] == game.remaining_moves

    """"
    Testing Gameboard's getBoard function
    """

    # testing with normal return value
    def test_getBoard1(self):

        with patch("db.getMove") as getMoveMock:
            # initializing game
            game = Gameboard.Gameboard()

            # set the return type of function call
            getMoveMock.return_value = [(
                "red",
                "[[0, 0, 0, 0, 0, 0, 0], " +
                "[0, 0, 0, 0, 0, 0, 0], " +
                "[0, 0, 0, 0, 0, 0, 0], " +
                "[0, 0, 0, 0, 0, 0, 0], " +
                "[0, 0, 0, 0, 0, 0, 0], " +
                "[0, 0, 0, 0, 0, 0, 0]]",
                "",
                "red",
                "yellow",
                "42"
            )]

            game.getBoard()

            assert game.current_turn == "red"
            assert str(game.board) == ("[[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0]]")
            assert game.game_result == ""
            assert game.player1 == "red"
            assert game.player2 == "yellow"

    # testing when there is nothing in db
    def test_getBoard2(self):

        with patch('db.getMove') as getMoveMock:

            # initializing gameboard
            game = Gameboard.Gameboard()

            getMoveMock.return_value = []

            try:
                game.getBoard()
                assert True
            except IndexError:
                assert False

    # testing with non-trivial values in gameboard
    def test_getBoard3(self):

        with patch("db.getMove") as getMoveMock:
            # initializing game
            game = Gameboard.Gameboard()

            # set the return type of function call
            getMoveMock.return_value = [(
                "yellow",
                "[[0, 0, 0, 'yellow', 0, 0, 0], " +
                "[0, 0, 0, 'red', 0, 0, 0], " +
                "['red', 0, 0, 'yellow', 0, 0, 0], " +
                "['red', 0, 'yellow', 'red', 0, 0, 0], " +
                "['red', 0, 'yellow', 'yellow', 0, 0, 0], " +
                "['red', 0, 'yellow', 'red', 0, 0, 0]]",
                "red",
                "red",
                "yellow",
                "29"
            )]

            game.getBoard()

            assert game.current_turn == 'yellow'
            assert str(game.board) == ("[[0, 0, 0, 'yellow', 0, 0, 0], " +
                                       "[0, 0, 0, 'red', 0, 0, 0], " +
                                       "['red', 0, 0, 'yellow', 0, 0, 0], " +
                                       "['red', 0, 'yellow', 'red'" +
                                       ", 0, 0, 0], " +
                                       "['red', 0, 'yellow', 'yellow'" +
                                       ", 0, 0, 0], " +
                                       "['red', 0, 'yellow', 'red', 0, 0, 0]]")
            assert game.game_result == 'red'
            assert game.player1 == 'red'
            assert game.player2 == 'yellow'
