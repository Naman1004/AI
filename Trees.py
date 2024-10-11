class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Function to insert a new node into the tree
def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

# In-order traversal of the tree (Left, Root, Right)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Pre-order traversal of the tree (Root, Left, Right)
def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Post-order traversal of the tree (Left, Right, Root)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

# Driver code to test the above functions
if __name__ == "__main__":
    root = None
    elements = [50, 30, 20, 40, 70, 60, 80]

    # Inserting nodes into the tree
    for element in elements:
        root = insert(root, element)

    print("In-order Traversal:")
    inorder_traversal(root)
    print("\nPre-order Traversal:")
    preorder_traversal(root)
    print("\nPost-order Traversal:")
    postorder_traversal(root)
