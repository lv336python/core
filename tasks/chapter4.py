"""
task_86a: Дано натуральное число n. Сколько цифр в числе n?
task107: Дано целое число m > 1. Получить наибольшее целое k, при котором 4^k < m .
"""


import math


def task_86a(num):
    """
    Accept one natural number
    Return amount of digits in number
    :param num: 444
    :return: 4
    """
    count = len(str(num))
    return count

def task_107(num):
    """
    Accept integer number m > 1
    Return the largest integer number kpow at which 4 in power kpow < num
    :param num: 4
    :return: 1
    """
    kpow = int(math.log(num, 4))

    if 4**kpow == num:
        return kpow-1
    return kpow
