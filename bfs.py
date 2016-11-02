G = [
	{1, 2, 3},
	{0, 4, 6},
	{0, 3},
	{0, 2, 4},
	{1, 3, 5, 6},
	{4, 7},
	{1, 4},
	{5}
]

from collections import deque

def bfs(G, v):
	q = deque([v])
	visited = set()
	visited.add(v)
	while q:
		u = q.popleft()
		print(u)
		for w in G[u]:
			if w not in visited:
				q.append(w)
				visited.add(w)

bfs(G, 0)

