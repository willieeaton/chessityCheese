#! python3
# chessityCheese.py - a silly little chessboard viewer - started Nov. 6, 2024
# P. Willie Eaton

# ask user to select between new game, PGN, and FEN
    # if empty board, create empty PGN and FEN
    # if FEN, store non-PGN flag
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
