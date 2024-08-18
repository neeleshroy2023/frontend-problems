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
	elif val > root.val:
		root.left = insert(root.left, val)
	return root

def remove(root, val):
	if not root:
		return None
	if val > root.val:
		root.right = remove(root.right, val)
	elif val > root.val:
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
 
def inorderTraversal(root):
	if root:
		inorderTraversal(root.left)
		print(root.val, end=" ")
		inorderTraversal(root.right)

driverNode = None

for value in [20, 40,30,50, 90, 60, 45]:
	insert(driverNode, value)

inorderTraversal(driverNode)

for value in [20, 50, 45]:
	remove(driverNode, value)
	inorderTraversal(driverNode)	
