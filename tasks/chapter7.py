def task_178_e(numbers):
	'''
	Function returns lenth of list of numbers a[k],
	in list a[1],......,a[n] where 2^k < a[k] < k!.
	'''
	from math import factorial
	k = 0
	list_a = []
	for a in numbers:
		k += 1
		if a > 2**k	and a<factorial(k):
			list_a.append(a)
	return len(list_a)



def task_243_b(num):
	'''
	Function finds all pairs of x, y for which x^2 + y^2 = num
	and x>=y.
	Return will be a list of tuples with pair x, y
	'''
	from math import sqrt 
	max_n = int(sqrt(num))+1 # will limit range and reduce check time
	pairs = []
	for x in range(1,max_n):
		for y in range(1,max_n):
			if x**2 + y**2 == num and x>=y: 
				pair = (x,y)
				pairs.append(pair)
	return pairs
