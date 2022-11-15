# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import numpy as np


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    O_win = 0  
    X_win = 0  

    # Check horizontal for how many X or O
    for row in board:
        count_O = 0
        count_X = 0
        for item in row:
            if item == 'O':
                count_O = count_O + 1  
            elif item == 'X':
                count_X = count_X + 1  
        if count_O == 3:
            O_win = O_win + 1   
        elif count_X == 3:
            X_win = X_win + 1   

    # Check vertical for how many X or O 
    board_trans = np.transpose(board) 
    for row in board_trans:
        count_O = 0
        count_X = 0
        for item in row:
            if item == 'O':
                count_O = count_O + 1  
            elif item == 'X':
                count_X = count_X + 1  
        if count_O == 3:
            O_win = O_win + 1   
        elif count_X == 3:
            X_win = X_win + 1  

    # Check diagnal for how many X or O
    count_O = 0
    count_X = 0
    for i in range(3):
        if board[i][i] == 'O':
            count_O = count_O + 1
        elif board[i][i] == 'X':
            count_X = count_X + 1

    if count_O == 3:
        O_win = O_win + 1
    elif count_X == 3:
        X_win = X_win + 1

    count_O = 0
    count_X = 0
    for i in range(3):
        if board[2 - i][i] == 'O':
            count_O = count_O + 1
        elif board[2 - i][i] == 'X':
            count_X = count_X + 1

    if count_O == 3:
        O_win = O_win + 1
    elif count_X == 3:
        X_win = X_win + 1


    if X_win > O_win:
        return 'X'
    elif X_win < O_win:
        return 'O'
    else:
        return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    else:
        return 'X'