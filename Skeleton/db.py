import sqlite3
from sqlite3 import Error

'''
Initializes the Table GAME
Do not modify
'''


def init_db():
    # creates Table
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute('CREATE TABLE GAME(current_turn TEXT, board TEXT,' +
                     'winner TEXT, player1 TEXT, player2 TEXT' +
                     ', remaining_moves INT)')
        print('Database Online, table created')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
move is a tuple (current_turn, board, winner, player1, player2,
remaining_moves)
Insert Tuple into table
'''


def add_move(move: tuple):  # will take in a tuple

    if type(move[5]) != int:
        raise TypeError("Last element in move argument must be int")
    for element in move[:5]:
        if type(element) != str:
            raise TypeError("All move elements except" +
                            " for the last element must string")

    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cur = conn.cursor()
        cur.execute('INSERT INTO GAME VALUES (?, ?, ?, ?, ?, ?)', move)
        conn.commit()
        print('Added move into database:')
        print('    ', move)
    except Error as e:
        raise e

    finally:
        if conn:
            conn.close()


'''
Get the last move played
return (current_turn, board, winner, player1, player2, remaining_moves)
'''


def getMove():
    # will return tuple(current_turn, board, winner, player1, player2,
    # remaining_moves) or None if db fails

    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM GAME ORDER BY remaining_moves LIMIT 1')
        print("Getting Gameboard object from DB")
        return cur.fetchall()
    except Error as e:
        print(e)
        return None


'''
Clears the Table GAME
Do not modify
'''


def clear():
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("DROP TABLE GAME")
        print('Database Cleared')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
