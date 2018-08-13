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
