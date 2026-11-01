class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def insert(self, root, key):
        # Normal BST insertion
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        # Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Balance the tree
        balance = self.get_balance(root)

        # Left-Left case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right-Right case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left-Right case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)


# Example usage
tree = AVLTree()
root = None

values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = tree.insert(root, value)

result = tree.search(root, 25)

if result:
    print("Value found:", result.key)
else:
    print("Value not found")
