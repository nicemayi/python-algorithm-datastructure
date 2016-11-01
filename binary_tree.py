class TreeNode(object):
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	def __repr__(self):
		return str(self.data)
	def __str__(self):
		return str(self.data)

A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
A.left = B
A.right = C
B.right = D
C.left = E
C.right = F
E.left = G
F.left = H
F.right = I
root = A

def preOrder(node):
	if not node:
		return
	print(node)
	preOrder(node.left)
	preOrder(node.right)

def inOrder(node):
	if not node:
		return
	preOrder(node.left)
	print(node)
	preOrder(node.right)

def postOrder(node):
	if not node:
		return
	preOrder(node.left)
	preOrder(node.right)
	print(node)

def preOrderIter(node):
	## backtracking method
	## use stack
	s = []
	node = root
	while True:
		while node:
			print(node)
			s.append(node)
			node = node.left
		if s == []:
			break
		node = s.pop().right

def inOrderIter(node):
	## backtracking method
	## use stack
	s = []
	node = root
	while True:
		while node:
			s.append(node)
			node = node.left
		## if node is None and s is empty, break
		if (not node) and (s == []):
			break
		node = s.pop()
		print(node)
		node = node.right

def postOrderIter(root):
	## backtracking method
	## use two stacks:
	## s1 is a auxiliary stack
	## s2 is the actual stack
	s1 = []
	s2 = []
	node = root
	s1.append(node)
	while s1: ## to generate real stack s2; visit s1 in order
		node = s1.pop()
		if node.left:
			s1.append(node.left)
		if node.right:
			s1.append(node.right)
		s2.append(node)
	while s2: ## visit node
		print(s2.pop())

def levelOrder(root):
	from collections import deque
	q = deque([root])
	while q:
		node = q.popleft()
		print(node)
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)

def depth(node):
	if node is None:
		return 0
	dl = depth(node.left)
	dr = depth(node.right)
	return max(dl, dr) + 1

def depthIter(node):
	from collections import deque
	q = deque([(root, 1)])
	while q:
		node, d = q.popleft()
		if node.left:
			q.append((node.left, d + 1))
		if node.right:
			q.append((node.right, d + 1))
	return d

def copyTree(node):
	if node is None:
		return
	lt = copyTree(node.left)
	rt = copyTree(node.right)
	return TreeNode(node.data, lt, rt)

def count_slow(n):
	## root : 1
	## left : k [0, n - 1]
	## right : n - 1 - k
	if n == 0 or n == 1:
		return 1
	s = 0
	for k in range(n):
		s += count_slow(k) * count_slow(n - 1 - k)
	return s


def count(n):
	## root : 1
	## left : k [0, n - 1]
	## right : n - 1 - k
	s = count.cache.get(n, 0)
	if s:
		return s
	s = 0
	for k in range(n):
		s += count(k) * count(n - 1 - k)
	count.cache[n] = s
	return s
count.cache = {0: 1, 1: 1}

if __name__ == "__main__":

	print("pre-order:")
	preOrder(root)
	print("in-order:")
	inOrder(root)
	print("post-order:")
	postOrder(root)

	print("pre-order-iter:")
	preOrderIter(root)
	print("in-order-iter:")
	inOrderIter(root)
	print("post-order-iter:")
	postOrderIter(root)

	print("level-order-iter:")
	levelOrder(root)

	print("depth:")
	print(depth(root))

	print("depth-iter:")
	print(depthIter(root))

	print("copy-tree:")
	copied_tree = copyTree(root)
	levelOrder(copied_tree)

	print("How many trees?")
	from datetime import datetime
	start_time = datetime.now()
	print(count(13))
	print("Cost: {} seconds!".format((datetime.now() - start_time).total_seconds()))
	start_time = datetime.now()
	print(count_slow(13))
	print("Cost: {} seconds!".format((datetime.now() - start_time).total_seconds()))