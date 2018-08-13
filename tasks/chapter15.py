def task_562():
	'''
	Fuction return all 2,3,4 digit narcissistic numbers
	(also known as Armstrong numbers)
	'''
	ppdi = []
	for num in range(10,10000):
		l_num = list(str(num)) # making number iterable 
		if num == sum([int(d)**len(l_num) for d in l_num]): # checking number to be narcissistic
			ppdi.append(num)
	return ppdi