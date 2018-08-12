import math


def task_86a(num):
    """
    Accept one natural number
    Return amount of digits in number
    :param num: 444
    :return: 4
    """

    if str(num).isdigit():
        count = len(str(num))
        return count
    else:
        return False

def task_107(m):
    """
    Accept integer number m > 1
    Return the largest integer number k at which 4 in power k < m
    :param m: 4
    :return: 1
    """

    k = int(math.log(m, 4))

    if 4**k == m:
        return k-1
    else:
        return k
