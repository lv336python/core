# by Volodymyr Petryna, Python 3.6.6

"""
Exercise 184
Даны целые числа p , q , a 1 , ... , a 67 ( p > q ≥ 0 ).
В последовательности a 1 , ... , a 67 заменить нулями члены, модуль
которых при делении на prn дает в остатке qrn. 2 Variants.
Exercise 242
Дано натуральное число n. Вычислить sum pow(-1, k*((k-1)/2)), k from 0 to n
"""
import math


def task_184(prn, qrn, *args):
    """
    Given numbers p, q and sequence a1, ...., a 67
    Return sequence where a[i]=0 if a[i] % p == q
    """
    if isinstance(prn, int) and isinstance(qrn, int):
        assert (prn > qrn >= 0) and len(args) < 68 #assert check
        args = list(args) #convert tuple to list cause tuple is immutable
        for i in args:
            if args[i] % prn == qrn:
                args[i] = 0
    else:
        raise TypeError
    return args


def task_184_1(prn, qrn, *args):
    """
    Given numbers p, q and sequence a1, ...., a 67
    Return sequence where a[i]=0 if a[i] % p == q
    """
    if isinstance(prn, int) and isinstance(qrn, int):
        assert (prn > qrn >= 0) and len(args) < 68
        args = list(args)
        index = 0
        while True:
            try:
                if args[index] % prn == qrn:
                    args[index] = 0
                index += 1
            except IndexError: #cause due to index step can be out of range error
                break
    else:
        raise TypeError
    return args




def task_242(num, the_sum=0):
    """
    Given n.
    Return sum pow(-1, k*((k-1)/2)), k from 0 to n
    """
    for k in range(num + 1):
        the_sum += ((math.pow(-1, k*((k-1)/2)))/math.factorial(num))
    return the_sum



def task_242_1(num, the_sum=0):
    """
    Given n.
    Return sum pow(-1, k*((k-1)/2)), k from 0 to n
    """
    def factorial(num):
        if num < 2:
            return 1
        return num * factorial((num - 1))
    for k in range(num + 1):
        the_sum += ((math.pow(-1, k*((k-1)/2)))/factorial(num))
    return the_sum
