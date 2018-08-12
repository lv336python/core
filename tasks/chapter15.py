import math


def is_even(num):
    """
    Returns True if number is even otherwise False
    :param num: 7
    :return: True
    """
    sqr_num = int(math.sqrt(num))
    for n in range(2, sqr_num+1):
        if num % n == 0:
            return False
    return True


def task_559(n):
    """
    Accepts any natural number
    Returns all natural numbers smaller than n that can be represented as 2**p-1, where p is an even
    :param n: 50000
    :return: [1, 3, 7, 31, 127, 2047, 8191]
    """
    if not isinstance(n, int):
        raise TypeError(f"must be int, not {type(n).__name__}")
    elif n < 1:
        raise ValueError("must be a natural number (bigger than 0)")
    max_p = int(math.log2(n))
    marsenne_nums = []
    for p in range(1, max_p):
        if is_even(p):
            marsenne_nums.append(2**p-1)
    return marsenne_nums

