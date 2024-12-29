class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if not root or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)


root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 20)

found_node = search(root, 20)
if found_node:
    print("Found:", found_node.key)
else:
    print("Not Found")
