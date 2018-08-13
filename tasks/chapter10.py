'''Tasks for chapter 10'''

def task_331_b(num):
    '''
    Function finds all triplets of x,y,z for which x^2 + y^2 + z^2= num.
    Return will be a list of tuples with x,y,z with all possible combinations.
    '''
    max_n = int(num**0.5)+1 # will limit range and reduce check time
    triplets = []
    for x_n in range(1, max_n):
        for y_n in range(1, max_n):
            for z_n in range(1, max_n):
                if x_n**2 + y_n**2 + z_n**2 == num:
                    triplet = (x_n, y_n, z_n)
                    triplets.append(triplet)
    return triplets
