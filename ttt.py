from copy import deepcopy
from functools import lru_cache


# def swap(s):
#     if s == 'o':
#         return 'x'
#     return 'o'

# def someone_won(board, w):
#     rows = [board[w*i:w*(i+1):1] for i in range(w)]
#     cols = [board[i::w] for i in range(w)]
#     diags = [board[0::w+1], board[w-1::w-1]]
#     for line in rows + cols + diags:
#         if all(cell == 'o' for cell in line):
#             return 'o'
#         if all(cell == 'x' for cell in line):
#             return 'x'
#     return False


# width = 3
# gameboard = [None for i in range(9)]
# game_over = 0
# x_or_o = "o"
# while not game_over:
#     player_guess = input(' --> ')
#     try:
#         player_move = int(player_guess)
#     except:
#         print("Enter an integer")
#         continue
#     if player_move < 0 or player_move > 8:
#         print("Enter a number between 0 and 8 inclusive")
#         continue
#     if gameboard[player_move]:
#         print("Enter a number which has not already been chosen")
#         continue
#     gameboard[player_move] = x_or_o
#     print(gameboard)
#     x_or_o = swap(x_or_o)
#     outcome = someone_won(gameboard, width)
#     if outcome:
#         game_over = 1
# #print("the winner is ", outcome)
    
# class TreeNode:
#     def __init__(self, parent):
#         self.parent = parent
#         self.children = []
#         if parent:
#             parent.children.append(self)

#     def tree_edges(self):
#         edge_set = []
#         kids = self.children 
#         for child in kids:
#             edge_set.append((child,self))
#             edge_set += child.tree_edges()
#         return edge_set            


# root = TreeNode(None)
# node1 = TreeNode(root)
# print(root.tree_edges())


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

#assume first player is computer

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
# board[0] = 'x'
# board[4] = 'o'
    
print(next_move(tuple(board), 'x', w))

    





            