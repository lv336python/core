# by Volodymyr Petryna, Python 3.6.6

"""
Exercise 184
Даны целые числа p , q , a 1 , ... , a 67 ( p > q ≥ 0 ). В последовательности a 1 , ... , a 67 заменить нулями члены, модуль
которых при делении на p дает в остатке q. 2 Variants.
Exercise 242
Дано натуральное число n. Вычислить sum pow(-1, k*((k-1)/2)), k from 0 to n
"""

def task_184(p, q, *args):
    """
    Given numbers p, q and sequence a1, ...., a 67
    Return sequence where a[i]=0 if a[i] % p == q
    """
    if isinstance(p, int) and isinstance(q, int):
        assert (p > q >= 0) and len(args) < 68 #assert check
        args = list(args) #convert tuple to list cause tuple is immutable
        for i in range(len(args)):
            if args[i] % p == q:
                args[i] = 0
    else:
        raise TypeError
    return args


def task_184_1(p, q, *args):
    """
    Given numbers p, q and sequence a1, ...., a 67
    Return sequence where a[i]=0 if a[i] % p == q
    """
    if isinstance(p, int) and isinstance(q, int):
        assert (p > q >= 0) and len(args) < 68
        args = list(args)
        index = 0
        while True:
            try:
                if args[index] % p == q:
                    args[index] = 0
                index += 1
            except IndexError: #cause due to index step can be out of range error
                break
    else:
        raise TypeError
    return args



import math

def task_242(n, sum=0):
    """
    Given n.
    Return sum pow(-1, k*((k-1)/2)), k from 0 to n
    """
    for k in range(n+1):
        sum += ((math.pow(-1, k*((k-1)/2)))/math.factorial(n))
    return sum



def task_242_1(n, sum=0):
    """
    Given n.
    Return sum pow(-1, k*((k-1)/2)), k from 0 to n
    """
    def factorial(n):
        if n < 2 and n >= 0:
            return 1
        else:
            return n * factorial((n - 1))
    for k in range(n+1):
        sum += ((math.pow(-1, k*((k-1)/2)))/factorial(n))
    return sum
