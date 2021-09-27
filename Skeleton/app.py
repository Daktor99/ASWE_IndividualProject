from flask import Flask, render_template, request, jsonify
from Gameboard import Gameboard
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

game = Gameboard()

'''
Implement '/' endpoint
Method Type: GET
return: template player1_connect.html and status = "Pick a Color."
Initial Webpage where gameboard is initialized
'''


@app.route('/', methods=['GET'])
def player1_connect():
    try:
        # make sure to reference global game variable
        global game
        game = Gameboard()

        return render_template("player1_connect.html", status='Pick a Color.')
    except Exception:
        return "Could not display player1_connect.html"


'''
Helper function that sends to all boards don't modify
'''


@app.route('/autoUpdate', methods=['GET'])
def updateAllBoards():
    try:
        return jsonify(move=game.board, winner=game.game_result,
                       color=game.player1)
    except Exception:
        return jsonify(move="")


'''
Implement '/p1Color' endpoint
Method Type: GET
return: template player1_connect.html and status = <Color picked>
Assign player1 their color
'''


@app.route('/p1Color', methods=['GET'])
def player1_config():
    try:
        # setting player1's color
        colorPicked = request.args['color']
        game.player1 = colorPicked

        return render_template('player1_connect.html',
                               status="Color picked: " + colorPicked)
    except Exception:
        return "Error with /p1Color"


'''
Implement '/p2Join' endpoint
Method Type: GET
return: template p2Join.html and status = <Color picked> or Error
if P1 didn't pick color first

Assign player2 their color
'''


@app.route('/p2Join', methods=['GET'])
def p2Join():
    try:

        if game.player1 == "red":
            game.player2 = p2Color = "yellow"
            return render_template("p2Join.html",
                                   status="Color picked: " + p2Color)
        elif game.player1 == "yellow":
            game.player2 = p2Color = "red"
            return render_template("p2Join.html",
                                   status="Color picked: " + p2Color)
        else:
            return render_template("p2Join.html",
                                   status="Error")

    except Exception:
        return "Error on '/p2join'"


'''
Implement '/move1' endpoint
Method Type: POST
return: jsonify (move=<CurrentBoard>,
invalid=True or False, winner = <currWinner>)
If move is valid --> invalid = False else invalid = True
If invalid == True, also return reason= <Why Move is Invalid>

Process Player 1's move
'''


@app.route('/move1', methods=['POST'])
def p1_move():

    # checking to see if the game is already over
    if game.game_result != "":
        return jsonify(move=game.board,
                       invalid=True,
                       reason="The game is already over, "
                              + game.game_result
                              + " has won!")

    # pull body from post request
    column = request.json['column']

    # if the move is not valid, return accordingly
    if game.remaining_moves == 0:
        return jsonify(move=game.board, invalid=True,
                       reason="No more moves to be made!",
                       winner=game.game_result)
    elif not game.isValidTurn("p1"):
        return jsonify(move=game.board,
                       invalid=True,
                       reason="Not your turn!",
                       winner=game.game_result)
    elif not game.isValidCol(column):
        return jsonify(move=game.board,
                       invalid=True,
                       reason="Cannot move here!",
                       winner=game.game_result)

    game.makeMove(column, game.player1)
    if game.checkIfWon(game.player1):
        game.game_result = 'p1'
    return jsonify(move=game.board,
                   invalid=False,
                   winner=game.game_result)


'''
Same as '/move1' but instead process Player 2
'''


@app.route('/move2', methods=['POST'])
def p2_move():

    # checking to see if the game is already over
    if game.game_result != "":
        return jsonify(move=game.board,
                       invalid=True,
                       reason="The game is already over, "
                              + game.game_result
                              + " has won!")

    # pull body from post request
    column = request.json['column']

    # if the move is not valid, return accordingly
    if game.remaining_moves == 0:
        return jsonify(move=game.board,
                       invalid=True,
                       reason="No more moves to be made. It's a draw!",
                       winner=game.game_result)
    elif not game.isValidTurn("p2"):
        return jsonify(move=game.board,
                       invalid=True,
                       reason="Not your turn!",
                       winner=game.game_result)
    elif not game.isValidCol(column):
        return jsonify(move=game.board,
                       invalid=True,
                       reason="Cannot move here!",
                       winner=game.game_result)

    game.makeMove(column, game.player2)
    if game.checkIfWon(game.player2):
        game.game_result = 'p2'
    return jsonify(move=game.board,
                   invalid=False,
                   winner=game.game_result)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
