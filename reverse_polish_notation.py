operators = {
	'+': lambda op1, op2: op1 + op2,
	'-': lambda op1, op2: op1 - op2,
	'*': lambda op1, op2: op1 * op2,
	'/': lambda op1, op2: op1 / op2
}

def evalPostFix(e):
	tokens = e.split()
	s = []
	for token in tokens:
		if token.isdigit():
			s.append(int(token))
		elif token in operators:
			f = operators[token]
			op2 = s.pop()
			op1 = s.pop()
			s.append(f(op1, op2))
	return s.pop()

if __name__ =="__main__":
	expr = "2 3 4 * +"
	print(evalPostFix(expr))