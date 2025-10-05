class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal:", end=" ")
inorder(root)
print()

# Explaination of Program

# Define a Node class with data, left, and right to represent each node of the tree.

# Define a function inorder(root) to traverse the tree in inorder (Left → Root → Right):

# If the current node exists:

# Recursively traverse the left subtree.

# Print the current node’s data.

# Recursively traverse the right subtree.

# Create the binary tree by connecting nodes:

# Root node = 1

# Left child of root = 2

# Right child of root = 3

# Left child of node 2 = 4

# Right child of node 2 = 5

# Print “Inorder Traversal:” and call inorder(root) to display the elements in inorder sequence.

# Output :- Inorder Traversal: 4 2 5 1 3

