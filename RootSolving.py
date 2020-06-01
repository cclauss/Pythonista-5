from math import *


class DomainError (Exception):
	def __init__(self):
		super().__init__('Something went wrong, likely a domain error. Try different initial(s) or a different method.')

		
class FunctionTypeError (Exception):
	def __init__(self):
		super().__init__('Please input a lambda function.')

				
class NoEnclosedRoot (Exception):
	def __init__(self):
		super().__init__('Chosen brackets do not enclose a single root. Choose different brackets.')


def printMaxIters(xr):
	print('Max iterations reached...')
	print(f'Function value at max iteration: {xr}')

	
def create_function(func):
	try:
		if type(func) == type(lambda x: x):
			name = func.__qualname__
			if name == '<lambda>':
				return (func)
		elif type(func) == str:
			func = eval(f"lambda x: {func}")
			return (func)
	except:
		raise FunctionTypeError
	else:
		raise FunctionTypeError


def Bisection(	func,
				xl,
				xu,
				Es=10e-12,
				max_iterations=500,
				print_iterations=False,
				print_xr=False):
	func = create_function(func)
	try:
		E = 100
		iterations = 0
		if func(xu) == 0:
			return (xu)
		elif func(xl) == 0:
			return (xl)
		if func(xu) * func(xl) > 0:
			raise NoEnclosedRoot
		else:
			while E > Es:
				iterations += 1
				if iterations >= max_iterations:
					printMaxIters(xr)
					return
				xr = (xl + xu) / 2
				if func(xr) == 0:
					break
				if func(xr) * func(xl) < 0:
					#root on lower
					xu = xr
				else:
					#root on upper
					xl = xr
				E = abs(func(xr))
				if print_xr == True:
					print(xr)
		if print_iterations == True:
			print(f'Iterations: {iterations}')
		return (xr)
	except:
		raise DomainError


def FalsePosition(	func,
					xl,
					xu,
					Es=10e-12,
					max_iterations=500,
					print_iterations=False,
					print_xr=False):
	func = create_function(func)
	try:
		E = 100
		iterations = 0
		if func(xl) == 0:
			return (xl)
		elif func(xu) == 0:
			return (xu)
		if func(xl) * func(xu) > 0:
			raise NoEnclosedRoot
		else:
			while E > Es:
				iterations += 1
				if iterations >= max_iterations:
					printMaxIters(xr)
					return
				xr = xu - func(xu) * (xu - xl) / (func(xu) - func(xl))
				if func(xr) == 0:
					break
				if func(xr) * func(xl) < 0:
					#root on lower
					xu = xr
				else:
					#root on upper
					xl = xr
				E = abs(func(xr))
				if print_xr == True:
					print(xr)
		if print_iterations == True:
			print(f'Iterations: {iterations}')
		return (xr)
	except:
		raise DomainError


def Ridders(func,
			xl,
			xu,
			Es=10e-12,
			max_iterations=500,
			print_iterations=False,
			print_xr=False):
	func = create_function(func)
	try:
		E = 100
		iterations = 0
		if func(xl) == 0:
			return (xl)
		elif func(xu) == 0:
			return (xu)
		if func(xl) * func(xu) > 0:
			raise NoEnclosedRoot
		else:
			while E > Es:
				iterations += 1
				if iterations >= max_iterations:
					printMaxIters(xd)
					return
				xr = (xl + xu) / 2
				if func(xr) == 0:
					xd = xr
					break
				xd = xr + (xr - xl) * copysign(func(xr), (func(xl) - func(xu))) / (
					func(xr)**2 - func(xl) * func(xu))**(1 / 2)
				if func(xd) == 0:
					break
				if func(xd) > 0:
					xu = xd
				else:
					xl = xd
				if print_xr == True:
					print(xd)
				E = abs(func(xd))
		if print_iterations == True:
			print(f'Iterations: {iterations}')
		return (xd)
	except:
		raise DomainError


def second_center_finite_difference(func, xg, h=1):
	func = create_function(func)
	return ((func(xg + h) - 2 * func(xg) + func(xg - h)) / h**2)


def center_finite_difference(func, xg, h=1):
	func = create_function(func)
	xu = xg + h / 2
	xl = xg - h / 2
	return ((func(xu) - func(xl)) / h)


def Newton(	func,
			x,
			Es=10e-12,
			max_iterations=500,
			print_iterations=False,
			print_xr=False):
	func = create_function(func)
	try:
		E = 100
		iterations = 0
		if func(x) == 0:
			return (x)
		while E > Es:
			iterations += 1
			if iterations >= max_iterations:
				printMaxIters(x)
				return
			x = x - func(x) / center_finite_difference(func, x)
			if func(x) == 0:
				break
			E = abs(func(x))
			if print_xr == True:
				print(x)
		if print_iterations == True:
			print(f"Iterations: {iterations}")
		return (x)
	except:
		raise DomainError


def Secant(	func,
			x0,
			x1,
			Es=10e-12,
			max_iterations=500,
			print_iterations=False,
			print_xr=False):
	func = create_function(func)
	try:
		E = 100
		iterations = 0
		if func(x0) == 0:
			return (x0)
		elif func(x1) == 0:
			return (x1)
		while E > Es:
			iterations += 1
			if iterations >= max_iterations:
				printMaxIters(x2)
				return
			x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
			E = abs(func(x2))
			if func(x2) == 0:
				break
			x0 = x1
			x1 = x2
			if print_xr == True:
				print(x2)
		if print_iterations == True:
			print(f"Iterations: {iterations}")
		return (x2)
	except:
		raise DomainError


def Halley(	func,
			x,
			Es=10e-12,
			max_iterations=500,
			print_iterations=False,
			print_xr=False):
	func = create_function(func)
	try:
		E = 100
		iterations = 0
		if func(x) == 0:
			return (x)
		while E > Es:
			iterations += 1
			if iterations >= max_iterations:
				printMaxIters(x)
				return
			fx_p = center_finite_difference(func, x)
			fx_2p = second_center_finite_difference(func, x)
			x = x - (2 * func(x) * fx_p) / (2 * fx_p**2 - func(x) * fx_2p)
			if func(x) == 0:
				break
			E = abs(func(x))
			if print_xr == True:
				print(x)
		if print_iterations == True:
			print(f"Iterations: {iterations}")
		return (x)
	except:
		raise DomainError


def Muller(	func,
			x1,
			x2,
			x3,
			Es=10e-12,
			max_iterations=500,
			print_iterations=False,
			print_xr=False):
	func = create_function(func)
	try:
		E = 100
		iterations = 0
		if func(x1) == 0:
			return (x1)
		elif func(x2) == 0:
			return (x2)
		elif func(x3) == 0:
			return (x3)
		while E > Es:
			iterations += 1
			if iterations >= max_iterations:
				printMaxIters(x4)
				return
			c = func(x3)
			d1 = func(x1) - func(x3)
			d2 = func(x2) - func(x3)
			h1 = x1 - x3
			h2 = x2 - x3
			b = (d2 * h1**2 - d1 * h2**2) / (h1 * h2 * (h1 - h2))
			a = (d1 * h2 - d2 * h1) / (h1 * h2 * (h1 - h2))
			den = b + sqrt(b**2 - 4 * a * c)
			if abs(den) < abs((b - sqrt(b**2 - 4 * a * c))):
				den = b - sqrt(b**2 - 4 * a * c)
			x4 = x3 - (2 * c) / den
			E = abs(func(x4))
			if func(x4) == 0:
				break
			if print_xr == True:
				print(x4)
			x1 = x2
			x2 = x3
			x3 = x4
		if print_iterations == True:
			print(f'Iterations: {iterations}')
		return (x4)
	except:
		raise DomainError


def Steffensen(	func,
				x,
				Es=10e-12,
				max_iterations=500,
				print_iterations=False,
				print_xr=False):
	func = create_function(func)
	try:
		E = 100
		iterations = 0
		if func(x) == 0:
			return (x)
		while E > Es:
			iterations += 1
			if iterations >= max_iterations:
				printMaxIters(x)
				return
			g = lambda x: func(x + func(x)) / func(x) - 1
			x = x - func(x) / g(x)
			E = abs(func(x))
			if func(x) == 0:
				break
			if print_xr == True:
				print(x)
		if print_iterations == True:
			print(f'Iterations: {iterations}')
		return (x)
	except:
		raise DomainError
