"""
This module is for tasks from chapter 7
"""
import math


def task_225(number):
    '''
    Accepts natural number
    Return all number from range <i = 1 to n >, if n % i*i == 0  and n % i*i*i != 0
    :param number: 54531 |   123456
    :return:  [3,]  |   [8,]
    '''
    return [i for i in range(1, number) if number % i ** 2 == 0 and number % i ** 3 != 0]


def task_182(*args):
    """Return sum and count of number could be divide 5 and not 7"""
    sum_element = 0
    count = 0
    for i in args:
        if i % 5 == 0 and i % 7 != 0:
            sum_element += i
            count += 1
    return {'sum': sum_element, 'count': count}


def task_241(power, number):
    """ Return list"""
    res = 0
    mid = 1
    while mid <= power:
        res += (((-1)**(math.sqrt(mid)) * number ** mid) / mid)
        mid += 1
    return res



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


def task_224(num):
    """
    Accept natural number num
    Return all natural dividers of num
    :param num: 25
    :return: 3
    """
    count = len([x for x in range(1, num + 1) if num % x == 0])
    return count
