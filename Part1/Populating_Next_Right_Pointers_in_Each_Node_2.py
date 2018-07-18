class TreeLinkNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution(object):
	def connect(self, root):
		dummy = TreeLinkNode(-1)
		node = dummy
		while root:
			while root:
				node.next = root.left
				node = node.next or node
				node.next = root.right
				node = node.next or node
				root = root.next
			root, node = dummy.next, dummy