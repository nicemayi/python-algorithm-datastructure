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

## recursive
def dfs(G, v, visited=set()):
	## use print to represent visit
	print(v)
	visited.add(v)
	for u in G[v]:
		if u not in visited:
			dfs(G, u, visited)

def dfsIter(G, v):
	visited = set()
	## need a stack (s) for back-tracking
	s = [v]
	while s:
		u = s.pop()
		if u not in visited:
			print(u)
			visited.add(u)
			[s.append(i) for i in G[u]]


dfs(G, 0)
print('-'*75)
dfsIter(G, 0)
