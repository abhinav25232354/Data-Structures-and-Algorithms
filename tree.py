class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert_left(self, current_node, value):
        current_node.left = TreeNode(value)
        return current_node.left

    def insert_right(self, current_node, value):
        current_node.right = TreeNode(value)
        return current_node.right

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def display_tree(self, node, space=0, LEVEL_SPACE=5):
        # Right child first (so tree looks correct when printed)
        if node is None:
            return
        space += LEVEL_SPACE
        self.display_tree(node.right, space)
        print()
        print(' ' * (space - LEVEL_SPACE) + str(node.data))
        self.display_tree(node.left, space)

# Create tree and insert nodes
bt = BinaryTree(1)
n2 = bt.insert_left(bt.root, 2)
n3 = bt.insert_right(bt.root, 3)
n4 = bt.insert_left(n2, 4)
n5 = bt.insert_right(n2, 5)
n6 = bt.insert_left(n3, 6)
n7 = bt.insert_right(n3, 7)

# Display tree
print("Binary Tree Structure:")
bt.display_tree(bt.root)

# Traversals
print("\nInorder Traversal:")
bt.inorder(bt.root)

print("\nPreorder Traversal:")
bt.preorder(bt.root)

print("\nPostorder Traversal:")
bt.postorder(bt.root)
