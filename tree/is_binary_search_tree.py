class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


prev = None


def check_bst_rec(root):
    global prev
    if root is None:
        return True

    if check_bst_rec(root.left) is False:
        return False

    if prev is not None and prev.data >= root.data:
        return False

    prev = root

    return check_bst_rec(root.right)


def tree_traverse(root):
    if root is not None:
        print(root.data)
        tree_traverse(root.left)
        tree_traverse(root.right)


def checkBST(root):
    # tree_traverse(root)
    global prev
    prev = None
    return check_bst_rec(root)


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(5)

print(checkBST(root))
