class TreeNode:
    def __init__(self, parent, name):
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)
        self.name = name

    def __repr__(self):
        return self.name

    def tree_edges(self):
        edge_set = []
        kids = self.children 
        for child in kids:
            edge_set.append((child,self))
            edge_set += child.tree_edges()
        return edge_set            


root = TreeNode(None,"root")
node1 = TreeNode(root, "1")

print((root.tree_edges()))
    