def move(a, b, c, n):
	if n == 1:
		print("{} -> {} : {}".format(a[0], b[0], c[0]))
		b.append(a.pop())
		return
	move(a, c, b, n - 1)
	b.append(a.pop())
	move(c, b, a, n - 1)

x = ['x', 5, 4, 3, 2, 1]
y = ['y', ]
z = ['z']

move(x, y, z, 5)
print(x, y, z)