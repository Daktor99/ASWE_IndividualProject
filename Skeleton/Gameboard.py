import db

class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42

    def isValidTurn(self, currPlayer: str) -> bool:

        if type(currPlayer) != str:
            raise TypeError

        if currPlayer not in ['p1', 'p2']:
            raise ValueError("Valid arguments to this function are either 'p1' or 'p2'")

        # check the correct player is making a move
        if self.current_turn != currPlayer:
            return False
        else:
            return True

    def isValidCol(self, column: str) -> bool:

        # get the integer representation of column string
        colNum = getColumnNum(column)

        # if we have any empty slot in the column, the move is valid
        for row in range(0, 6):
            if self.board[row][colNum] == 0:
                return True

        # if we don't find any free slots in the column, move is not valid
        return False

    def changeTurn(self):

        if self.current_turn == 'p1':
            self.current_turn = 'p2'
        elif self.current_turn == 'p2':
            self.current_turn = 'p1'
        else:
            raise ValueError("current_turn is something other than 'p1' or 'p2', this is not allowed")
        return

    def makeMove(self, column: str, currPlayer: str):

        playerColor = currPlayer
        colNum = getColumnNum(column)

        # place in the lowest available slot
        for row in range(0, 6):
            if self.board[5 - row][colNum] == 0:
                self.board[5 - row][colNum] = playerColor
                break

        self.remaining_moves -= 1
        self.changeTurn()

        return

    def checkIfWon(self, playerColor: str):

        if self.checkHorizontal(playerColor) or self.checkVertical(playerColor) or self.checkDiagonal(playerColor):
            return True

        return False

    def checkHorizontal(self, playerColor: str):

        for row in range(0, 6):
            countInARow = 0
            for col in range(0, 7):
                if self.board[row][col] == playerColor:
                    countInARow += 1
                else:
                    countInARow = 0

                # 4 in a row found horizontally, return True
                if countInARow == 4:
                    return True

        # 4 in a row not found horizontally, return False
        return False

    def checkVertical(self, playerColor: str):

        for col in range(0, 7):
            countInARow = 0
            for row in range(0, 6):
                if self.board[row][col] == playerColor:
                    countInARow += 1
                else:
                    countInARow = 0

                # if we found 4 in a row vertically, return true
                if countInARow == 4:
                    return True

        # 4 in a row not found vertically, return false
        return False

    def checkDiagonal(self, playerColor: str):

        # checking diagonals going \
        for row in range(0, 3):
            for col in range(0, 4):
                if playerColor == self.board[row][col] and self.board[row+1][col+1] == playerColor and self.board[row+2][col+2] == playerColor and self.board[row+3][col+3] == playerColor:
                    return True

        # checking diagonals going /
        for row in range(0, 3):
            for col in range(3, 7):
                if playerColor == self.board[row][col] and self.board[row+1][col-1] == playerColor and self.board[row+2][col-2] == playerColor and self.board[row+3][col-3] == playerColor:
                    return True

        # no diagonal found, return false
        return False



'''
Add Helper functions as needed to handle moves and update board and turns
'''

"""
    
"""
def getColumnNum(col_string: str) -> int:

    if len(col_string) != 4 or col_string[0:3] != 'col':
        # checking to make sure col_string has "col#" as formatting
        raise ValueError("Needs to be passed string in format 'col#' where # = 1-7")
    elif int(col_string[3]) not in range(1, 8):
        # checking to make sure col_string has column within range of the board
        raise ValueError("Column number passed must be between 1-7.")

    return int(col_string[3]) - 1
