# chessityCheese.py
a silly little chessboard viewer

Just a practice project to keep my mind sharp and let me play around with some chess notation and algorithm.

## Currently capable of:
- Decoding the piece positions in a pasted FEN format chess position, or creating a new game board state
- Displaying a very basic diagram of the board with ASCII characters

## To-Do

### Very short term
- Determine which and whose turn the position is
- Determine if the position is illegal, in-play, in-play but in check, drawn to stalemate, drawn to other rules, or in checkmate
- Extract the remainder of information from FEN files

### Short term
- Enable read/write of full PGN games
- Allow player to add moves to end of game
- Add input from file in addition to clipboard

### Medium term
- Implement some very simple computer chess algorithms (inspired by the Tom7/suckerpinch "Elo World" video)
- Enable human vs human, human vs CPU, and CPU vs CPU full games
