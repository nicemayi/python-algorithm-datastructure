G = [
	{1: 28, 5: 10},			# 0
	{0: 28, 2: 16, 6: 14},	# 1
	{1: 16, 3: 12},			# 2
	{2: 12, 4: 22, 6: 18},	# 3
	{3: 22, 5: 25, 6: 24},	# 4
	{0: 10, 4: 25},			# 5
	{1: 14, 3: 18, 4: 24},	# 6
	# {}
]

import heapq

def prim(G, start_v = 0):
	n = len(G)
	v = start_v
	s = set()
	s.add(v)
	edges = []
	res = []
	for _ in range(n - 1):
		for u, w in G[v].items():
			heapq.heappush(edges, (w, v, u))

		while edges:
			w, p, q = heapq.heappop(edges)
			if q not in s:
				s.add(q)
				res.append(((p, q), w))
				v = q
				break
		else:
			raise Exception("not connected graph!")
	return res

prim_tree = prim(G)
print(prim_tree)
print("Price is: {}".format(sum([i[1] for i in prim_tree])))