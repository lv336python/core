"""
    Module with chapter 15 tasks
"""

import math


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
