"""
This module is for tasks from chapter 15
"""
import math
from itertools import product


def task_555(number):
    '''
    Accepts natural number
    Return Pascal triangle
    :param number: 4
    :return:                [1]
                           [1, 1]
                         [1, 2, 1]
                        [1, 3, 3, 1]

    '''
    tringle = [[1], [1, 1]]
    for _ in range(2, number):
        next_row = [1]

        for j in range(len(tringle[-1]) - 1):
            next_row.append(tringle[-1][j] + tringle[-1][j + 1])

        tringle.append(next_row)
        tringle[-1].append(1)
    return tringle


def expr(list_op):
    """Return formated string"""
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*list_op)


def gen_expr():
    """Return product for ['+', '-', ''] """
    operators = ['+', '-', '']
    return [expr(var) for var in product(operators, repeat=9) if var[0] != '+']


def task_568(val):
    """Return all possible variant for val"""
    for res_string in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expr())): # pylint: disable=eval-used
        print(res_string)


def task_569(num):
    """
    Given a natural number n.
    Return sequence of numbers that % (2,3,5) == 0
    """
    count = 0
    k = 1
    result = ''
    while count != num:
        if k % 2 == 0 or k % 3 == 0 or k % 5 == 0:
            result = result + ' ' + str(k)
            count += 1
        k += 1
    return result


def task_569_check(num):
    """
    Given a natural number n.
    Return sequence of numbers that % (2,3,5) == 0
    """
    sequence_list = []
    for i in range(1, num + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            sequence_list.append(i)
            sequence_tuple = tuple(sequence_list)#sequence in one row
    return sequence_tuple


def is_even(num):
    """
    Returns True if number is even otherwise False
    :param num: 7
    :return: True
    """
    sqr_num = int(math.sqrt(num))
    for number in range(2, sqr_num+1):
        if num % number == 0:
            return False
    return True


def task_559(num):
    """
    Accepts any natural number
    Returns all natural numbers smaller than n that can be represented as 2**p-1, where p is an even
    :param num: 50000
    :return: [1, 3, 7, 31, 127, 2047, 8191]
    """
    max_p = int(math.log2(num))
    marsenne_nums = []
    for p_val in range(1, max_p):
        if is_even(p_val):
            marsenne_nums.append(2**p_val-1)
    return marsenne_nums
