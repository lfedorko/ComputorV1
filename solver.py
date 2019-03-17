def solve(equ):
	if degree == 0:
		print( 'Degree 0 – non-zero constant')	
	elif degree == 1:
		pass
	elif degree == 2:
		solve_quadratic(a, b, c)

def solve_linear(b, c):
	print( 'Degree 1 – linear')
	if a == 0:
		if b == 0:
			print("True for all X")
		else:
			print("No solutions")
	else:
		if b == 0:
			print("X = 0")
		else:
			print("X = " + b / a)

def solve_quadratic(a, b, c):
	print( 'Degree 2 – quadratic')
	D = b * b - 4 * a * c
	if D > 0:
		x1 = (-b + (D ** .5)) / (2 * a * c)
		x2 = (-b - (D ** .5)) / (2 * a * c)
		print("D = {}\nX1 = {}\nX2 = {}" .format(D, x1, x2))
	elif D == 0:
		x = -b / 2 * a
		print("D = 0\nX = {}\n".format(x))	
	else:
		print("There is no solution!")
