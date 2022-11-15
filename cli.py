# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from typing import List
from logic import make_empty_board, get_winner, other_player
from thegame import *
import copy

def print_board(board):
    display_board = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if display_board[i][j] is not None:
                display_board[i][j] = display_board[i][j]
            else:
                display_board[i][j] = "-"
        print(display_board[i])

if __name__ == '__main__':
    game = SinglePlayerGame()
    game.game_loop()