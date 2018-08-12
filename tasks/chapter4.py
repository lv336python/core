def task_88_a(n):
    """
    Accepts one natural number
    Returns True if number n**2 contain digit 3, returns False if number n**2 does not contain digit 3
    :param n: 19
    :return: True
    """
    num = set([x for x in str(n ** 2)])
    return '3' in num
