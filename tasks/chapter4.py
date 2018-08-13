"""
    Module with chapter 4 tasks
"""

def task_87(num, num_of_digits):
    """
    Accepts two natural numbers n and m
    Returns sum of the last m digits of number n
    :param num: 7242
    :param num_of_digits: 2
    :return: 8
    """
    return sum([int(digit) for digit in str(num)[-num_of_digits::]])
