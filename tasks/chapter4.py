def task_86_b(number):
    '''
    Accepts natural number.
    Returns sum of number digits.
    :param number: 354
    :return:  12
    '''
    return sum([int(i) for i in list(str(number))])


def task_108(n):
    '''
    Accepts natural number.
    Return the first number like 2^r which is greater than our number
    :param n:   3   |   453
    :return:    4   |   512
    '''
    power = 0
    while (True):
        if 2 ** power > n:
            break
        else:
            power += 1
    return 2 ** power
