from copy import deepcopy
from functools import lru_cache


def game_over(board, w):
    rows = [ board[i : i+w] for i in range(0, w*w, w) ]
    cols = [ board[j::w] for j in range(w) ]
    diags = [ board[0::w+1], board[w-1:w**2-1:w-1] ]
    for line in rows + cols + diags:
        if all(cell == 'o' for cell in line):
            return 'o'
        if all(cell == 'x' for cell in line):
            return 'x'
    if any(not cell for cell in board):
        return False
    return 'tie'


@lru_cache(maxsize = None)
def next_move(state, turn, w):
    children = []
    winner = game_over(state, w)
    if winner:
        return (None, winner)
    if turn == 'o':
        next_turn ='x'
    else:
        next_turn ='o'
    for i, cell in enumerate(state):
        if not cell:
            current_child = list(state)
            current_child[i] = turn
            _, winner = next_move(tuple(current_child), next_turn, w)
            children.append((i, winner))

    def key(elem):
        _, winner = elem
        if winner == turn:
            return 1
        if winner == 'tie':
            return 0
        return -1

    return max(children, key=key)

w = 4
dim = 2
board = [None for _ in range(w**dim)]
    
print(next_move(tuple(board), 'x', w))

    





            