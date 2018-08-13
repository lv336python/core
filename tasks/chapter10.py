"""
    Module with chapter 10 tasks
"""

def task_329(num_1, num_2):
    """
    Accepts two natural numbers
    Returns all numbers that are smaller than n and square
    number of sum of digits of which are equal m
    :param num_1: 51
    :param num_2: 25
    :return: [50, 41, 32, 23, 14, 5]
    """
    sqr_root = num_2 ** 0.5
    result = []
    for num in range(num_1, 0, -1):
        if sum(int(digit) for digit in str(num)) == sqr_root:
            result.append(num)
    return result
