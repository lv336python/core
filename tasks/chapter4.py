""" Chapter 4"""


def task_88_h(number):
    """ Return int"""
    number = str(number)
    if not number.isdigit():
        return 'Enter a valid number'
    return int('1' + number + '1')
