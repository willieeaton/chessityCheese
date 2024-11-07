#! python3
# chessityCheese.py - a silly little chessboard viewer - started Nov. 6, 2024
# P. Willie Eaton
import pyinputplus as pyip
import pyperclip, re

def decodeFen(fenPosition):
    squares = [[' ' for x in range(8)] for y in range(8)]
    rowRegex = re.compile('(\w+\/)(\w+\/)(\w+\/)(\w+\/)(\w+\/)(\w+\/)(\w+\/)(\w+)')
    rows = rowRegex.search(fenPosition)
    for i in rows.groups():
        rowSquares = [' ' for x in range(8)]
        j = 0
        while (j < 8):
            if str.isdigit(i[j]):
                j += int(i[j])
            elif i[j]=='/':
                    j = 8
            else:
                pieceRegex = re.compile('[pnbrqkPNBRQK]')
                pr = pieceRegex.search(i[j])
                if pr:
                    rowSquares[j] = i[j]
                    j += 1
                else:
                    # error - unknown symbol in the rows
                    pass
        squares[rows.groups().index(i)] = rowSquares
    return squares

def displayBoard():
    for i in range(8):
        for j in range(8):
            print(squares[i][j], end='')
        print('')

squares = [[' ' for x in range(8)] for y in range(8)]
# ask user to select between new game, PGN, and FEN
print('Would you like to:\n1. Begin with a new game of chess\n2. Paste a FEN game state\n3. Paste a PGN format game')
result = pyip.inputInt(min=1, max=3)
if result == 1:
    # if new game, initialize board, and create FEN and PGN
    fenPosition = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    squares = decodeFen(fenPosition)
    displayBoard()
if result == 2:
    # if FEN, store non-PGN flag
    pgnPosition = False
    # if PGN, store PGN in variable

# read chess game
    # if FEN, construct position and check for legality
    # if PGN, play through game, checking all moves for legality

# display chess game

# menu of next options
# 1) move a piece
# 8) export FEN position
# 9) (if PGN or new game) export PGN game
# 0) exit game

# def movePiece():
    # check legality of move
        # piece type can move that way
            # includes two square pawn move, en passant, and castling
        # position is legal
            # does not leave king in check or pass a castling king through check
    # if PGN, append to PGN
    # update board state
    # construct FEN
    # return to display game
