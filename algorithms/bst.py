class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def getMinValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def remove(root, val):
    if not root:
        return None
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minValueNode = getMinValueNode(root.right)
            root.val = minValueNode.val
            root.right = remove(root.right, minValueNode.val)
    return root

# Driver code
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)

root = None

values = [50,30,20,40,70,60,80]
for value in values:
    root = insert(root, value)

printInorder(root)
print("\n")

for value in [20, 30, 50]:
    root = remove(root, value)
    printInorder(root)
    print("\n")
