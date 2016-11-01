from binary_tree import TreeNode, levelOrder

class BinarySearchTree(object):

	def __init__(self):
		self.root = None

	def search(self, k):
		node, _ = self._search(k)
		return node

	def _search(self, k):
		parent = None
		node = self.root
		while node and node.data != k:
			parent = node
			if k < node.data:
				node = node.left
			else:
				node = node.right
		return node, parent

	def insert(self, k):
		node, parent = self._search(k)
		if node:
			return
		node = TreeNode(k)
		if parent is None:
			self.root = node
		elif k < parent.data:
			parent.left = node
		else:
			parent.right = node

	def delete(self, k):
		pass


if __name__ == "__main__":
	bst = BinarySearchTree()
	data = [10, 5, 15, 1, 8, 12, 2]
	[bst.insert(each) for each in data]
	# levelOrder(bst.root)
	print('-'*20)
	print(bst.search(17))