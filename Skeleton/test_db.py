import unittest
import db
import Gameboard
from sqlite3 import Error


class Test_Testdb(unittest.TestCase):
    """
    Testing db's init_db()
    """

    def setUp(self):
        db.init_db()
        return

    def tearDown(self):
        db.clear()
        return

    # testing normal add move functionality: move is valid
    def test_add_move1(self):

        try:
            # initializing gameboard
            game = Gameboard.Gameboard()
            move = game.getMove()
            db.add_move(move)
            assert True
        except Error:
            assert False

    # testing invalid move parameter: remaining moves is string
    def test_add_move2(self):
        try:
            # initializing gameboard
            game = Gameboard.Gameboard()
            move = game.getMove()

            # change remaining moves to be string instead of int
            move = list(move)
            move[5] = "42"
            move = tuple(move)

            db.add_move(move)
            assert False
        except TypeError:
            assert True

    # testing invalid move parameter: current turn is not string
    def test_add_move3(self):
        try:

            # initializing gameboard
            game = Gameboard.Gameboard()
            move = game.getMove()

            # change remaining moves to be string instead of int
            move = list(move)
            move[0] = 13
            move = tuple(move)

            db.add_move(move)
            assert False
        except TypeError:
            assert True

    # testing invalid move parameter: move has length of 7
    def test_add_move4(self):
        try:

            # initializing gameboard
            game = Gameboard.Gameboard()
            move = game.getMove()

            # change remaining moves to be string instead of int
            move = list(move)
            move.append("garbage_value")
            move = tuple(move)

            db.add_move(move)
            assert False
        except Error:
            assert True

    # testing add move when db does not exist
    def test_add_move5(self):

        try:
            # clear the db
            db.clear()

            # try adding move to db that doesn't exist
            game = Gameboard.Gameboard()
            db.add_move(game.getMove())
            assert False
        except Error:
            assert True

    """
    Testing db's getMove function
    """

    # testing normal functionality: initial move exists
    def test_get_move1(self):
        try:

            # initializing gameboard & adding move
            game = Gameboard.Gameboard()
            game.setP1Color("red")

            db.add_move(game.getMove())

            game.getBoard()

            assert game.current_turn == "p1"
            assert game.player1 == "red"
            assert game.player2 == "yellow"
            assert game.remaining_moves == 42
            assert game.game_result == ""
            assert str(game.board) == ("[[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0], " +
                                       "[0, 0, 0, 0, 0, 0, 0]]")
        except Error:
            assert False

    # testing getMove when db doesn't exist
    def test_get_move2(self):

        try:
            # initializing gameboard & adding move
            game = Gameboard.Gameboard()
            db.clear()
            # should return None if db fails
            assert not db.getMove()

            # should raise TypeError: Object not subscriptable if no db
            game.getBoard()
            assert False
        except TypeError:
            assert True

    # test to make sure that the DB always only returns one result
    def test_get_move3(self):

        # initializing gameboard
        game = Gameboard.Gameboard()
        game.setP1Color('red')
        db.add_move(game.getMove())

        move = db.getMove()

        assert len(move) == 1


if __name__ == '__main__':
    unittest.main()
