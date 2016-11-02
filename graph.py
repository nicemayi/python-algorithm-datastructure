from pdb import set_trace as bp

## adjancent matrix
N = 5
a, b, c, d, e = range(N)
G = [[0]*N for _ in range(N)]

def addEdge(G, v1, v2, weight = 1):
	G[v1][v2] = G[v2][v1] = weight

addEdge(G, a, b)
addEdge(G, a, e)
addEdge(G, b, d)
addEdge(G, b, c)
addEdge(G, b, e)
addEdge(G, d, e)
addEdge(G, d, c)

## adjancent dictionary
G2 = [{b, e}, {a, e, d, c}, {b, d}, {b, c, e}, {a, b, d}]
# print(G2[b])

## adjancent dictionary with weighting
G3 = [
	{
		b: 4,
		e: 2
	}, {
		a: 4,
		c: 5,
		d: 6,
		e: 3
	}, {
		b: 5,
		d: 1
	}, {
		b: 6,
		c: 5,
		e: 1
	}, {
		a: 2,
		b: 3,
		d: 1
	}
]