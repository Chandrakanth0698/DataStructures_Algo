class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        temp = self.root
        if self.root is None:
            self.root = Node(value)
            return True
        while True:
            if value == temp.value:
                return False
            if value > temp.value:
                if temp.right is None:
                    temp.right = Node(value)
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = Node(value)
                    return True
                temp = temp.left


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""

print('Root:', my_tree.root.value)
print('Root->Left:', my_tree.root.left.value)
print('Root->Right:', my_tree.root.right.value)

"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""
