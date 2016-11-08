LEFT = {'(', '[', '{'}
RIGHT = {')', ']', '}'}

def match(expr):
	s = []
	for c in expr:
		if c in LEFT:
			s.append(c)
		elif c in RIGHT:
			if not s:
				return False
			if c == ')':
				if s[-1] == '(':
					s.pop()
				else:
					return False
			if c == ']':
				if s[-1] == '[':
					s.pop()
				else:
					return False
			if c == '}':
				if s[-1] == '{':
					s.pop()
				else:
					return False
	return not s


if __name__ == "__main__":
	expr = "{}"
	print(match(expr))

