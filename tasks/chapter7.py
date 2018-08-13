"""Tasks for chapter 7"""


def task_178_e(numbers):
    '''
    Function returns lenth of list of numbers a[k],
    in list a[1],......,a[n] where 2^k < a[k] < k!.
    '''
    from math import factorial
    pos_n = 0
    list_a = []
    for a_k in numbers:
        pos_n += 1
        if 2**pos_n < a_k < factorial(pos_n):
            list_a.append(a_k)
    return len(list_a)



def task_243_b(num):
    '''
    Function finds all pairs of x, y for which x^2 + y^2 = num
    and x>=y.
    Return will be a list of tuples with pair x, y
    '''
    max_n = int(num**0.5)+1 # will limit range and reduce check time
    pairs = []
    for x_n in range(1, max_n):
        for y_n in range(1, max_n):
            if x_n**2 + y_n**2 == num and x_n >= y_n:
                pair = (x_n, y_n)
                pairs.append(pair)
    return pairs
# print(task_243_b(625))
# print(task_178_e([1,2,3,5,4,6,100,548]))
