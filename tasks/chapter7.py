def task_243_b(num):
	'''
	Function finds all pairs of x, y for which x^2 + y^2 = num
	and x>=y.
	Return will be a list of tuples with pair x, y
	'''
	from math import sqrt 
	max_n = int(sqrt(num)) # will limit range and reduce check time
	pairs = []
	for x in range(1,max_n):
		for y in range(1,max_n):
			if x**2 + y**2 == num and x>=y: 
				pair = (x,y)
				pairs.append(pair)
	return pairs
