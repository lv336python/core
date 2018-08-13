"""
    Accepts one natural number
    Returns True if number n**2 contain digit 3,\
    returns False if number n**2 does not contain digit 3
    :param n_value: 19
    :return: True
"""


def task_88_a(n_value):
    """Check if number contain digit '3'"""
    num = list(str(n_value**2))
    return '3' in num
