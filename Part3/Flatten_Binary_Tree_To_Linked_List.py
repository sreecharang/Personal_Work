class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def flatten(self, root):
		stack = []
		while root:
			if root.left:
				if root.right:
					stack.append(root.right)
				root.right, root.left = root.left, None
			if not root.right and stack:
				root.right = stack.pop()
			root = root.right
			