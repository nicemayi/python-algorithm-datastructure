G = {
	"C1": ["C3", "C8"],
	"C2": ["C3", "C4", "C5"],
	"C3": ["C4"],
	"C4": ["C6", "C7"],
	"C5": ["C6"],
	"C6": [],
	"C7": [],
	"C8": ["C9"],
	"C9": ["C7"],
}

def topological_sort(G):
	indegrees = {v: 0 for v in G}
	## first get indegrees for all vertices
	for al in G.values():
		for v in al:
			indegrees[v] += 1
	q = [v for v in G if indegrees[v] == 0]
	## list head = 0
	i = 0
	while i < len(q):
		for v in G[q[i]]:
			indegrees[v] -= 1
			if indegrees[v] == 0:
				q.append(v)
		i += 1
	return q if i== len(G) else None


print(topological_sort(G))