def task_331_b(num):
	'''
	Function finds all triplets of x,y,z for which x^2 + y^2 + z^2= num.
	Return will be a list of tuples with x,y,z with all possible combinations.
	'''
	from math import sqrt 
	max_n = int(sqrt(num))+1 # will limit range and reduce check time
	triplets = []
	for x in range(1,max_n):
		for y in range(1,max_n):
			for z in range(1,max_n):
				if x**2 + y**2 + z**2 == num:
					triplet = (x,y,z)
					triplets.append(triplet)
	return triplets