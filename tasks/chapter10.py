"""
    Accepts natural number
    Returns True if n is perfect number and False if n is not perfect number
    :param x_values: 6
    :return: True
"""


def task_330(x_values):
    """ Returns True if n is perfect number and False if n is not perfect number"""
    sum1 = 0
    for i in range(1, x_values - 1):
        if x_values % i == 0:
            sum1 += i
    return sum1 == x_values
