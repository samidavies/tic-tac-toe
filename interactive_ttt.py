def swap(s):
    if s == 'o':
        return 'x'
    return 'o'

def someone_won(board, w):
    rows = [board[w*i:w*(i+1):1] for i in range(w)]
    cols = [board[i::w] for i in range(w)]
    diags = [board[0::w+1], board[w-1::w-1]]
    for line in rows + cols + diags:
        if all(cell == 'o' for cell in line):
            return 'o'
        if all(cell == 'x' for cell in line):
            return 'x'
    return False


width = 3
gameboard = [None for i in range(9)]
game_over = 0
x_or_o = "o"
while not game_over:
    player_guess = input(' --> ')
    try:
        player_move = int(player_guess)
    except:
        print("Enter an integer")
        continue
    if player_move < 0 or player_move > 8:
        print("Enter a number between 0 and 8 inclusive")
        continue
    if gameboard[player_move]:
        print("Enter a number which has not already been chosen")
        continue
    gameboard[player_move] = x_or_o
    print(gameboard)
    x_or_o = swap(x_or_o)
    outcome = someone_won(gameboard, width)
    if outcome:
        game_over = 1
print("the winner is ", outcome)
    
class TreeNode:
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)

    def tree_edges(self):
        edge_set = []
        kids = self.children 
        for child in kids:
            edge_set.append((child,self))
            edge_set += child.tree_edges()
        return edge_set            


root = TreeNode(None)
node1 = TreeNode(root)