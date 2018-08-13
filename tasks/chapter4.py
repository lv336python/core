"""
This module is for task from chapter 4
"""


def task_86_b(number):
    '''
    Accepts natural number.
    Returns sum of number digits.
    :param number: 354
    :return:  12
    '''
    return sum([int(i) for i in list(str(number))])


def task_108(number):
    '''

    Accepts natural number.
    Return the first number like 2^r which is greater than our number
    :param number:   3   |   453
    :return:    4   |   512
    '''
    power = 0
    while True:
        if 2 ** power > number:
            break
        else:
            power += 1
    return 2 ** power


def task_88_h(number):
    """ Return int"""
    number = str(number)
    if not number.isdigit():
        return 'Enter a valid number'
    return int('1' + number + '1')
