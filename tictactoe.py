"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    flattened_board = [item for el in board for item in el]

    if (flattened_board.count(EMPTY) % 2 != 0):
        return X
    return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possibleActions.add((row, col))
    
    return possibleActions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = deepcopy(board);
    i, j = action

    move = player(newBoard)

    newBoard[i][j] = move

    return newBoard

    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if all(item == X for item in row):
            return X
        if all(item == O for item in row):
            return O
    
    columns = []
    for index in range(len(board)):
        columns.append([row[index] for row in board])
    
    for col in columns:
        if all(item == X for item in col):
            return X
        if all(item == O for item in col):
            return O
    
    leftToRight = [row[index] for index, row in enumerate(board)]
    rightToLeft = [row[-index - 1] for index, row in enumerate(board)]

    if all(item == X for item in leftToRight):
        return X
    if all(item == X for item in rightToLeft):
        return X
    if all(item == O for item in leftToRight):
        return O
    if all(item == O for item in rightToLeft):
        return O

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    
    if winner(board) == O:
        return -1

    return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # print(board)
    # print(winner(board))

    if terminal(board):
        return utility(board)
    

    if player(board) == X:
        v = -math.inf
        # bestAction = None
        for action in actions(board):
            # if minimax(result(board, action)) > v:
                # bestAction = action
            v = max(v, minimax(result(board, action)))
        return v
    else:
        v = math.inf
        # bestAction = None
        for action in actions(board):
            # if minimax(result(board, action)) < v:
            #     v = minimax(result(board, action))
                # bestAction = action
            v = min(v, minimax(result(board, action)))
        return v

